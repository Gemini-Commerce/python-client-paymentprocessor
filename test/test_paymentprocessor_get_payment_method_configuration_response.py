# coding: utf-8

"""
    Payment Processor Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from paymentprocessor.models.paymentprocessor_get_payment_method_configuration_response import PaymentprocessorGetPaymentMethodConfigurationResponse

class TestPaymentprocessorGetPaymentMethodConfigurationResponse(unittest.TestCase):
    """PaymentprocessorGetPaymentMethodConfigurationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentprocessorGetPaymentMethodConfigurationResponse:
        """Test PaymentprocessorGetPaymentMethodConfigurationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentprocessorGetPaymentMethodConfigurationResponse`
        """
        model = PaymentprocessorGetPaymentMethodConfigurationResponse()
        if include_optional:
            return PaymentprocessorGetPaymentMethodConfigurationResponse(
                configuration = None
            )
        else:
            return PaymentprocessorGetPaymentMethodConfigurationResponse(
        )
        """

    def testPaymentprocessorGetPaymentMethodConfigurationResponse(self):
        """Test PaymentprocessorGetPaymentMethodConfigurationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
