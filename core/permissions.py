from rest_framework.permissions import BasePermission


class DefaultGlobalPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        permission = self.__get_permission_name(request.method, view)
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return user.has_perm(permission)

        if request.method == 'POST':
            return user.has_perm(permission)
        
        if request.method in ['PUT', 'PATCH']:
            return user.has_perm(permission)        

        if request.method == 'DELETE':
            return user.has_perm(permission)

        return False
    

    def __get_permission_name(self, method, view):
        model_name = view.queryset.model._meta.model_name
        app_label = view.queryset.model._meta.app_label
        action = self.__get_action_sufix(method)

        return f'{app_label}.{action}_{model_name}'
    
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'OPTIONS': 'view',
            'HEAD': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
        }

        return method_actions.get(method, '')