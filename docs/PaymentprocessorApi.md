# paymentprocessor.PaymentprocessorApi

All URIs are relative to *https://payment-processor.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_payment**](PaymentprocessorApi.md#authorize_payment) | **POST** /paymentprocessor.Paymentprocessor/AuthorizePayment | Authorize Payment
[**create_payment_method**](PaymentprocessorApi.md#create_payment_method) | **POST** /paymentprocessor.Paymentprocessor/CreatePaymentMethod | Create Payment Method
[**finalize_payment**](PaymentprocessorApi.md#finalize_payment) | **POST** /paymentprocessor.Paymentprocessor/FinalizePayment | Finalize Payment
[**get_available_payment_method**](PaymentprocessorApi.md#get_available_payment_method) | **POST** /paymentprocessor.Paymentprocessor/GetAvailablePaymentMethod | Get Available Payment Method
[**get_payment_method**](PaymentprocessorApi.md#get_payment_method) | **POST** /paymentprocessor.Paymentprocessor/GetPaymentMethod | Get Payment Method
[**get_payment_method_configuration**](PaymentprocessorApi.md#get_payment_method_configuration) | **POST** /paymentprocessor.Paymentprocessor/GetPaymentMethodConfiguration | Get Payment Method Configuration
[**init_payment**](PaymentprocessorApi.md#init_payment) | **POST** /paymentprocessor.Paymentprocessor/InitPayment | Init Payment
[**list_available_payment_methods**](PaymentprocessorApi.md#list_available_payment_methods) | **POST** /paymentprocessor.Paymentprocessor/ListAvailablePaymentMethods | List Available Payment Methods
[**list_payment_methods**](PaymentprocessorApi.md#list_payment_methods) | **POST** /paymentprocessor.Paymentprocessor/ListPaymentMethods | List Payment Methods
[**perform_payment**](PaymentprocessorApi.md#perform_payment) | **POST** /paymentprocessor.Paymentprocessor/PerformPayment | Perform Payment
[**perform_refund**](PaymentprocessorApi.md#perform_refund) | **POST** /paymentprocessor.Paymentprocessor/PerformRefund | Perform Refund
[**update_payment**](PaymentprocessorApi.md#update_payment) | **POST** /paymentprocessor.Paymentprocessor/UpdatePayment | Update Payment
[**update_payment_method**](PaymentprocessorApi.md#update_payment_method) | **POST** /paymentprocessor.Paymentprocessor/UpdatePaymentMethod | Update Payment Method
[**void_payment**](PaymentprocessorApi.md#void_payment) | **POST** /paymentprocessor.Paymentprocessor/VoidPayment | Void Payment


# **authorize_payment**
> PaymentprocessorAuthorizePaymentResponse authorize_payment(body)

Authorize Payment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_authorize_payment_request import PaymentprocessorAuthorizePaymentRequest
from paymentprocessor.models.paymentprocessor_authorize_payment_response import PaymentprocessorAuthorizePaymentResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorAuthorizePaymentRequest() # PaymentprocessorAuthorizePaymentRequest | 

    try:
        # Authorize Payment
        api_response = api_instance.authorize_payment(body)
        print("The response of PaymentprocessorApi->authorize_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->authorize_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorAuthorizePaymentRequest**](PaymentprocessorAuthorizePaymentRequest.md)|  | 

### Return type

[**PaymentprocessorAuthorizePaymentResponse**](PaymentprocessorAuthorizePaymentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_method**
> PaymentprocessorPaymentMethod create_payment_method(body)

Create Payment Method

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_create_payment_method_request import PaymentprocessorCreatePaymentMethodRequest
from paymentprocessor.models.paymentprocessor_payment_method import PaymentprocessorPaymentMethod
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorCreatePaymentMethodRequest() # PaymentprocessorCreatePaymentMethodRequest | 

    try:
        # Create Payment Method
        api_response = api_instance.create_payment_method(body)
        print("The response of PaymentprocessorApi->create_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->create_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorCreatePaymentMethodRequest**](PaymentprocessorCreatePaymentMethodRequest.md)|  | 

### Return type

[**PaymentprocessorPaymentMethod**](PaymentprocessorPaymentMethod.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_payment**
> PaymentprocessorFinalizePaymentResponse finalize_payment(body)

Finalize Payment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_finalize_payment_request import PaymentprocessorFinalizePaymentRequest
from paymentprocessor.models.paymentprocessor_finalize_payment_response import PaymentprocessorFinalizePaymentResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorFinalizePaymentRequest() # PaymentprocessorFinalizePaymentRequest | 

    try:
        # Finalize Payment
        api_response = api_instance.finalize_payment(body)
        print("The response of PaymentprocessorApi->finalize_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->finalize_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorFinalizePaymentRequest**](PaymentprocessorFinalizePaymentRequest.md)|  | 

### Return type

[**PaymentprocessorFinalizePaymentResponse**](PaymentprocessorFinalizePaymentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_payment_method**
> PaymentprocessorPaymentMethod get_available_payment_method(body)

Get Available Payment Method

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_get_available_payment_method_request import PaymentprocessorGetAvailablePaymentMethodRequest
from paymentprocessor.models.paymentprocessor_payment_method import PaymentprocessorPaymentMethod
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorGetAvailablePaymentMethodRequest() # PaymentprocessorGetAvailablePaymentMethodRequest | 

    try:
        # Get Available Payment Method
        api_response = api_instance.get_available_payment_method(body)
        print("The response of PaymentprocessorApi->get_available_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->get_available_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorGetAvailablePaymentMethodRequest**](PaymentprocessorGetAvailablePaymentMethodRequest.md)|  | 

### Return type

[**PaymentprocessorPaymentMethod**](PaymentprocessorPaymentMethod.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> PaymentprocessorPaymentMethod get_payment_method(body)

Get Payment Method

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_get_payment_method_request import PaymentprocessorGetPaymentMethodRequest
from paymentprocessor.models.paymentprocessor_payment_method import PaymentprocessorPaymentMethod
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorGetPaymentMethodRequest() # PaymentprocessorGetPaymentMethodRequest | 

    try:
        # Get Payment Method
        api_response = api_instance.get_payment_method(body)
        print("The response of PaymentprocessorApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->get_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorGetPaymentMethodRequest**](PaymentprocessorGetPaymentMethodRequest.md)|  | 

### Return type

[**PaymentprocessorPaymentMethod**](PaymentprocessorPaymentMethod.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_configuration**
> PaymentprocessorGetPaymentMethodConfigurationResponse get_payment_method_configuration(body)

Get Payment Method Configuration

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_get_payment_method_configuration_request import PaymentprocessorGetPaymentMethodConfigurationRequest
from paymentprocessor.models.paymentprocessor_get_payment_method_configuration_response import PaymentprocessorGetPaymentMethodConfigurationResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorGetPaymentMethodConfigurationRequest() # PaymentprocessorGetPaymentMethodConfigurationRequest | 

    try:
        # Get Payment Method Configuration
        api_response = api_instance.get_payment_method_configuration(body)
        print("The response of PaymentprocessorApi->get_payment_method_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->get_payment_method_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorGetPaymentMethodConfigurationRequest**](PaymentprocessorGetPaymentMethodConfigurationRequest.md)|  | 

### Return type

[**PaymentprocessorGetPaymentMethodConfigurationResponse**](PaymentprocessorGetPaymentMethodConfigurationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **init_payment**
> PaymentprocessorInitPaymentResponse init_payment(body)

Init Payment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_init_payment_request import PaymentprocessorInitPaymentRequest
from paymentprocessor.models.paymentprocessor_init_payment_response import PaymentprocessorInitPaymentResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorInitPaymentRequest() # PaymentprocessorInitPaymentRequest | 

    try:
        # Init Payment
        api_response = api_instance.init_payment(body)
        print("The response of PaymentprocessorApi->init_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->init_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorInitPaymentRequest**](PaymentprocessorInitPaymentRequest.md)|  | 

### Return type

[**PaymentprocessorInitPaymentResponse**](PaymentprocessorInitPaymentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_payment_methods**
> PaymentprocessorListAvailablePaymentMethodsResponse list_available_payment_methods(body)

List Available Payment Methods

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_list_available_payment_methods_request import PaymentprocessorListAvailablePaymentMethodsRequest
from paymentprocessor.models.paymentprocessor_list_available_payment_methods_response import PaymentprocessorListAvailablePaymentMethodsResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorListAvailablePaymentMethodsRequest() # PaymentprocessorListAvailablePaymentMethodsRequest | 

    try:
        # List Available Payment Methods
        api_response = api_instance.list_available_payment_methods(body)
        print("The response of PaymentprocessorApi->list_available_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->list_available_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorListAvailablePaymentMethodsRequest**](PaymentprocessorListAvailablePaymentMethodsRequest.md)|  | 

### Return type

[**PaymentprocessorListAvailablePaymentMethodsResponse**](PaymentprocessorListAvailablePaymentMethodsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_methods**
> PaymentprocessorListPaymentMethodsResponse list_payment_methods(body)

List Payment Methods

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_list_payment_methods_request import PaymentprocessorListPaymentMethodsRequest
from paymentprocessor.models.paymentprocessor_list_payment_methods_response import PaymentprocessorListPaymentMethodsResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorListPaymentMethodsRequest() # PaymentprocessorListPaymentMethodsRequest | 

    try:
        # List Payment Methods
        api_response = api_instance.list_payment_methods(body)
        print("The response of PaymentprocessorApi->list_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->list_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorListPaymentMethodsRequest**](PaymentprocessorListPaymentMethodsRequest.md)|  | 

### Return type

[**PaymentprocessorListPaymentMethodsResponse**](PaymentprocessorListPaymentMethodsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_payment**
> PaymentprocessorPerformPaymentResponse perform_payment(body)

Perform Payment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_perform_payment_request import PaymentprocessorPerformPaymentRequest
from paymentprocessor.models.paymentprocessor_perform_payment_response import PaymentprocessorPerformPaymentResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorPerformPaymentRequest() # PaymentprocessorPerformPaymentRequest | 

    try:
        # Perform Payment
        api_response = api_instance.perform_payment(body)
        print("The response of PaymentprocessorApi->perform_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->perform_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorPerformPaymentRequest**](PaymentprocessorPerformPaymentRequest.md)|  | 

### Return type

[**PaymentprocessorPerformPaymentResponse**](PaymentprocessorPerformPaymentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_refund**
> object perform_refund(body)

Perform Refund

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_perform_refund_request import PaymentprocessorPerformRefundRequest
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorPerformRefundRequest() # PaymentprocessorPerformRefundRequest | 

    try:
        # Perform Refund
        api_response = api_instance.perform_refund(body)
        print("The response of PaymentprocessorApi->perform_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->perform_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorPerformRefundRequest**](PaymentprocessorPerformRefundRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> object update_payment(body)

Update Payment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_update_payment_request import PaymentprocessorUpdatePaymentRequest
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorUpdatePaymentRequest() # PaymentprocessorUpdatePaymentRequest | 

    try:
        # Update Payment
        api_response = api_instance.update_payment(body)
        print("The response of PaymentprocessorApi->update_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->update_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorUpdatePaymentRequest**](PaymentprocessorUpdatePaymentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> PaymentprocessorPaymentMethod update_payment_method(body)

Update Payment Method

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_payment_method import PaymentprocessorPaymentMethod
from paymentprocessor.models.paymentprocessor_update_payment_method_request import PaymentprocessorUpdatePaymentMethodRequest
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorUpdatePaymentMethodRequest() # PaymentprocessorUpdatePaymentMethodRequest | 

    try:
        # Update Payment Method
        api_response = api_instance.update_payment_method(body)
        print("The response of PaymentprocessorApi->update_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->update_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorUpdatePaymentMethodRequest**](PaymentprocessorUpdatePaymentMethodRequest.md)|  | 

### Return type

[**PaymentprocessorPaymentMethod**](PaymentprocessorPaymentMethod.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_payment**
> PaymentprocessorVoidPaymentResponse void_payment(body)

Void Payment

### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import paymentprocessor
from paymentprocessor.models.paymentprocessor_void_payment_request import PaymentprocessorVoidPaymentRequest
from paymentprocessor.models.paymentprocessor_void_payment_response import PaymentprocessorVoidPaymentResponse
from paymentprocessor.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://payment-processor.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = paymentprocessor.Configuration(
    host = "https://payment-processor.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with paymentprocessor.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paymentprocessor.PaymentprocessorApi(api_client)
    body = paymentprocessor.PaymentprocessorVoidPaymentRequest() # PaymentprocessorVoidPaymentRequest | 

    try:
        # Void Payment
        api_response = api_instance.void_payment(body)
        print("The response of PaymentprocessorApi->void_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentprocessorApi->void_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentprocessorVoidPaymentRequest**](PaymentprocessorVoidPaymentRequest.md)|  | 

### Return type

[**PaymentprocessorVoidPaymentResponse**](PaymentprocessorVoidPaymentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

