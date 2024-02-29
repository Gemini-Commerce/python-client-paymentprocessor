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

from paymentprocessor.models.paymentprocessor_payment_method_restriction_condition import PaymentprocessorPaymentMethodRestrictionCondition

class TestPaymentprocessorPaymentMethodRestrictionCondition(unittest.TestCase):
    """PaymentprocessorPaymentMethodRestrictionCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentprocessorPaymentMethodRestrictionCondition:
        """Test PaymentprocessorPaymentMethodRestrictionCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentprocessorPaymentMethodRestrictionCondition`
        """
        model = PaymentprocessorPaymentMethodRestrictionCondition()
        if include_optional:
            return PaymentprocessorPaymentMethodRestrictionCondition(
                context_path = '',
                action = 'DISALLOW',
                condition = 'IN',
                values = [
                    ''
                    ]
            )
        else:
            return PaymentprocessorPaymentMethodRestrictionCondition(
        )
        """

    def testPaymentprocessorPaymentMethodRestrictionCondition(self):
        """Test PaymentprocessorPaymentMethodRestrictionCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
