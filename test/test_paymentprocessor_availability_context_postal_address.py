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

from paymentprocessor.models.paymentprocessor_availability_context_postal_address import PaymentprocessorAvailabilityContextPostalAddress

class TestPaymentprocessorAvailabilityContextPostalAddress(unittest.TestCase):
    """PaymentprocessorAvailabilityContextPostalAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentprocessorAvailabilityContextPostalAddress:
        """Test PaymentprocessorAvailabilityContextPostalAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentprocessorAvailabilityContextPostalAddress`
        """
        model = PaymentprocessorAvailabilityContextPostalAddress()
        if include_optional:
            return PaymentprocessorAvailabilityContextPostalAddress(
                region_code = '',
                postal_code = '',
                firstname = '',
                lastname = '',
                address_lines = [
                    ''
                    ],
                additional_info = paymentprocessor.models.additional_info.additionalInfo()
            )
        else:
            return PaymentprocessorAvailabilityContextPostalAddress(
        )
        """

    def testPaymentprocessorAvailabilityContextPostalAddress(self):
        """Test PaymentprocessorAvailabilityContextPostalAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
