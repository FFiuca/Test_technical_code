from django.shortcuts import render
from django import forms
from rest_framework import viewsets, response
from . import forms as form_validation, service as function_service
# Create your views here.

class CalculateView(viewsets.ViewSet):

    def calculate_segitiga(self, request):
        data = request.data
        # print(data)

        result = None
        try:
            validate = form_validation.FormValidation(data=data)
            if validate.is_valid() is False:
                raise forms.ValidationError("form has error")

            cls = function_service.CalculateService(data.get("number"))
            result = cls.calculate_segitiga()


        except forms.ValidationError:
            return response.Response({
                'status': 400,
                'data': {
                    'message': validate.errors
                }
            }, status=400)
        except Exception as e:
            return response.Response({
                'status': 500,
                'data': {
                    'message': e.__str__()
                }
            }, status=500)

        return response.Response({
            'status': 200,
            'data': result
        }, status=200)

    def calculate_ganjil(self, request):
        data = request.data

        result = None
        try:
            validate = form_validation.FormValidation(data=data)
            if validate.is_valid() is False:
                raise forms.ValidationError("form has error")

            cls = function_service.CalculateService(data.get("number"))
            result = cls.calculate_ganjil()


        except forms.ValidationError:
            return response.Response({
                'status': 400,
                'data': {
                    'message': validate.errors
                }
            }, status=400)
        except Exception as e:

            return response.Response({
                'status': 500,
                'data': {
                    'message': e.__str__()
                }
            }, status=500)

        return response.Response({
            'status': 200,
            'data': result
        }, status=200)


    def calculate_prima(self, request):
        data = request.data

        result = None
        try:
            validate = form_validation.FormValidation(data=data)
            if validate.is_valid() is False:
                raise forms.ValidationError("form has error")

            cls = function_service.CalculateService(data.get("number"))
            result = cls.calculate_prima()


        except forms.ValidationError as e:
            return response.Response({
                'status': 400,
                'data': {
                    'message': validate.errors
                }
            }, status=400)
        except Exception as e:
            return response.Response({
                'status': 500,
                'data': {
                    'message': e.__str__()
                }
            }, status=500)

        return response.Response({
            'status': 200,
            'data': result
        }, status=200)
