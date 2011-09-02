from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.template import Template, RequestContext


def list(request, content_type, id):
    """
    Wrapper exposing comment's render_comment_list tag as a view.
    """
    # get object
    app_label, model = content_type.split('-')
    ctype = ContentType.objects.get(app_label=app_label, model=model)
    obj = ctype.get_object_for_this_type(id=id)

    # setup template and return result
    t = Template("{% load comments %}{% render_comment_list for object %}")
    context = RequestContext(request)
    context.update({'object': obj})
    result = t.render(context)
    return HttpResponse(result)
