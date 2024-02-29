# coding: utf-8

"""
    Payment Processor Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from paymentprocessor.models.availability_context_customer import AvailabilityContextCustomer
from paymentprocessor.models.paymentprocessor_availability_context_postal_address import PaymentprocessorAvailabilityContextPostalAddress
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PaymentprocessorAvailabilityContext(BaseModel):
    """
    PaymentprocessorAvailabilityContext
    """ # noqa: E501
    shipping_address: Optional[PaymentprocessorAvailabilityContextPostalAddress] = Field(default=None, alias="shippingAddress")
    billing_address: Optional[PaymentprocessorAvailabilityContextPostalAddress] = Field(default=None, alias="billingAddress")
    customer: Optional[AvailabilityContextCustomer] = None
    __properties: ClassVar[List[str]] = ["shippingAddress", "billingAddress", "customer"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentprocessorAvailabilityContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PaymentprocessorAvailabilityContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shippingAddress": PaymentprocessorAvailabilityContextPostalAddress.from_dict(obj.get("shippingAddress")) if obj.get("shippingAddress") is not None else None,
            "billingAddress": PaymentprocessorAvailabilityContextPostalAddress.from_dict(obj.get("billingAddress")) if obj.get("billingAddress") is not None else None,
            "customer": AvailabilityContextCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None
        })
        return _obj


