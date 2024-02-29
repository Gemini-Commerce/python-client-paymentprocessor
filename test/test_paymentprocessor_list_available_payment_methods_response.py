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

from paymentprocessor.models.paymentprocessor_list_available_payment_methods_response import PaymentprocessorListAvailablePaymentMethodsResponse

class TestPaymentprocessorListAvailablePaymentMethodsResponse(unittest.TestCase):
    """PaymentprocessorListAvailablePaymentMethodsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentprocessorListAvailablePaymentMethodsResponse:
        """Test PaymentprocessorListAvailablePaymentMethodsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentprocessorListAvailablePaymentMethodsResponse`
        """
        model = PaymentprocessorListAvailablePaymentMethodsResponse()
        if include_optional:
            return PaymentprocessorListAvailablePaymentMethodsResponse(
                methods = [
                    paymentprocessor.models.paymentprocessor_payment_method.paymentprocessorPaymentMethod(
                        code = '', 
                        title = paymentprocessor.models.paymentprocessor_localized_text.paymentprocessorLocalizedText(
                            value = {
                                'key' : ''
                                }, ), 
                        label = paymentprocessor.models.paymentprocessor_localized_text.paymentprocessorLocalizedText(), 
                        enabled = True, 
                        amount = paymentprocessor.models.paymentprocessor_money.paymentprocessorMoney(
                            units = '', 
                            micros = 56, ), 
                        currency = 'XXX', 
                        additional_info = '', 
                        is_upfront = True, 
                        description = , 
                        restrictions = [
                            paymentprocessor.models.paymentprocessor_payment_method_restriction.paymentprocessorPaymentMethodRestriction(
                                conditions = [
                                    paymentprocessor.models.paymentprocessor_payment_method_restriction_condition.paymentprocessorPaymentMethodRestrictionCondition(
                                        context_path = '', 
                                        action = 'DISALLOW', 
                                        condition = 'IN', 
                                        values = [
                                            ''
                                            ], )
                                    ], )
                            ], )
                    ]
            )
        else:
            return PaymentprocessorListAvailablePaymentMethodsResponse(
        )
        """

    def testPaymentprocessorListAvailablePaymentMethodsResponse(self):
        """Test PaymentprocessorListAvailablePaymentMethodsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
