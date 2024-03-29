from django.shortcuts import render
from app.models import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework import status

# Create your views here.

class EmployeeCrud(ViewSet):

    # Here we are using list method in this method we are getting all the employee details are present on our database
    # if there is any employee is not found means am raising the error called internal server error
    # Here I am using exceptional handling for handling the perticular data if everythings works well means am getting all the list of all employee details
    # if there is no any error in try block it will excecute the data in response, otherwise we are handling the error by using except block
    def list(self, request):
        try:
            employees = Employee.objects.all()
            serializer = EmployeeModelSerializer(employees, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




    # Here we are using the retrieve method for getting specific  employee details instead of all employees
    # By using Employee id we are getting perticular employee details
    # If you give any unidentified ID no means am raising the error employee not found
    # Any exception from internally example files and json parser error am raising the internal server error 
    def retrieve(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeModelSerializer(employee)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




    
    # Here we are using create method for creating the new employee details
    # We are create new employee details by two ways in admin user interface and by using post method after successfully executed the code
    # While creating the details it will checking the validation data whether you are fallowing the instructions based on our key constaints
    # After validating successfully means we are successfully created the employee details successfullyy and returns the data as a response
    # Incase any error(Not fallow the rules we mentioned some data types and constarint) while creating the employee details it raises the bad request
    # Here we are handling the error in except block if there is any other exceptions in our code it raises the bad request
    # We are using try except blocks if there is no error in try block it will returns the response otherwise we are handling the error in except block and raises the internal server error
    def create(self, request):
        try:
            serializer = EmployeeModelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Employee created'},status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        




    # Here we are using update method for updating the new employee details or existing employee details by using employye id number
    # if we want to do more than  one updated columns means we are using the update method 
    # Update method will works in PUT method,if you get all employee details after running the server then there is option name called put for updating the data
    # It take all existed employee details for updating another employee details then it will update the data
    # While updating the details it will checking the validation data whether you are fallowing the instructions based on our key constaints 
    # in this there one minor mistake is there for updating the data we are dealing photo field in our json data if you want to update the data including you photo field it will raises format issues file handling issues
    # If everything is done correctly and fallow all validations rules when we are trying to update the data it will successfully updated the data 
    # if will come across any errors while updating the data the am raising the error called bad request
    # Any execptions related to employee details not found in our database then am raising Employee not found
    # there is any other exceptions means am raising error called internal server error 
    # we are using try except blocks if there is  no errors in our it will successfully updated the data otherwise it raise the exception.
    def update(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeModelSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Employee updated'},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



    # Here we are using partial_update method for updating existing employee details by using employye id number
    # here we are dealing to update specific fields for that we using  partial_update the data
    # partial_Update method will works in PATCH method,After getting perticular employee details there a option called PATCH for updation
    # While partial_updating the details it will checking the validation data whether you are fallowing the instructions based on our key constaints
    # if validations are everything works fine means then we are partially_updated the data
    # if we want to change name of the employee details then we have copy the only name column for updating the data
    # Here after validating the data then we return a response a employee partially updated successfully
    # If any errors means I am raising the error as bad request
    # There is no employee found in perticular ID then i am raising not found error
    #There is any other exception then we are raising Internal server error
    def partial_update(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeModelSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Employee partially updated'},status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)






    # we are performing delete operation for deleting an existing employee fallowed by employeeID
    # by using ID getting employee details in order to delete that there is an option after getting ID 
    # it will delete the particular employee details successfully
    # if no employee found with perticular employeeID then am raising the not found error
    # we are handling other exeception for storing internal server error 
    def destroy(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return Response({'message': 'Employee deleted'},status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

