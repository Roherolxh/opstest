# Create your views here.
# -*- coding: utf-8 -*-

from rest_framework.views import APIView

from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.generators import LinkNode, insert_into
from rest_framework.renderers import *
from rest_framework_swagger import renderers
from rest_framework.response import Response

# from rest_framework.schemas import SchemaGenerator
class MySchemaGenerator(SchemaGenerator):

    def get_links(self, request=None):
        # from rest_framework.schemas.generators import LinkNode,
        links = LinkNode()

        paths = []
        view_endpoints = []
        for path, method, callback in self.endpoints:
            view = self.create_view(callback, method, request)
            path = self.coerce_path(path, method, view)
            paths.append(path)
            view_endpoints.append((path, method, view))

        # Only generate the path prefix for paths that will be included
        if not paths:
            return None
        prefix = self.determine_path_prefix(paths)

        for path, method, view in view_endpoints:
            if not self.has_view_permissions(path, method, view):
                continue
            link = view.schema.get_link(path, method, base_url=self.url)
            # 添加下面这一行方便在views编写过程中自定义参数.
            link._fields += self.get_core_fields(view)

            subpath = path[len(prefix):]
            keys = self.get_keys(subpath, method, view)

            # from rest_framework.schemas.generators import LinkNode, insert_into
            insert_into(links, keys, link)

        return links

    # 从类中取出我们自定义的参数, 交给swagger 以生成接口文档.
    def get_core_fields(self, view):
        return getattr(view, 'coreapi_fields', ())

def DocParam(name="default", location="query", required=True, description=None, type="string", *args, **kwargs):
    return coreapi.Field(name=name, location=location, required=required, description=description, type=type)


class ReturnJson(APIView):
	"""
	retrieve:
		Return a user instance.
	"""
	coreapi_fields = (
		DocParam("name", description='test'),
		DocParam("nalanxiao", required=False, description='rohero'),
	)
	def get(self, request, *args, **kwargs):
		json_data = {'name': 'post', 'id': 0}
		return Response(json_data)

	def post(self, request, *args, **kwargs):
		json_data = {'name': 'post', 'id': 0}
		return Response(json_data)

class SwaggerSchemaView(APIView):
    _ignore_model_permissions = True
    exclude_from_schema = True

    # from rest_framework.permissions import AllowAny
    permission_classes = [AllowAny]
    # from rest_framework_swagger import renderers
    # from rest_framework.renderers import *
    renderer_classes = [
        CoreJSONRenderer,
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = MySchemaGenerator(title='纳兰晓', description='''v1.0.0''')
        schema = generator.get_schema(request=request)
        # from rest_framework.response import Response
        return Response(schema)


class StudentsApiView(APIView):
	coreapi_fields = (
		DocParam("name", description='test'),
		DocParam("nalanxiao", required=False, description='rohero'),
	)

	def get(self,request,format=None):
		json_data = {'name': 'get', 'id': 1}
		return Response(json_data)

	def post(self,request, format=None):
		"""
		retrieve:
        	Return a user instance.
		"""
		json_data = {'name': 'post', 'id': 0}
		return Response(json_data)