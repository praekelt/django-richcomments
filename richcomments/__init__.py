from django.contrib.comments.templatetags.comments import \
        RenderCommentFormNode, RenderCommentListNode
from django.template.loader import render_to_string


def rendercommentform_render_wrapper(func):
    def wrapped(self, context, *args, **kwargs):
        ctype, object_pk = self.get_target_ctype_pk(context)
        selector_id = "%s%s" % (ctype.model, object_pk)
        return  render_to_string("richcomments/form_js.html", {
            "form_html": func(self, context, *args, **kwargs),
            "selector_id": selector_id,
            "content_type": "-".join((ctype.app_label, ctype.model)),
            "object_pk": object_pk,
        })
    return wrapped

RenderCommentFormNode.render = rendercommentform_render_wrapper(\
        RenderCommentFormNode.render)


def rendercommentlist_render_wrapper(func):
    def wrapped(self, context, *args, **kwargs):
        ctype, object_pk = self.get_target_ctype_pk(context)
        selector_id = "commentlist_%s%s" % (ctype.model, object_pk)
        return  render_to_string("richcomments/list_wrapper.html", {
            "list_html": func(self, context, *args, **kwargs),
            "selector_id": selector_id,
        })
    return wrapped

RenderCommentListNode.render = rendercommentlist_render_wrapper(\
        RenderCommentListNode.render)
