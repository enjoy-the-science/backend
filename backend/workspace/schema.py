import marshmallow
from marshmallow import fields


class AuthRequestSchema(marshmallow.Schema):
    dicom_uid = fields.Str(required=False, data_key='dicom-uid')
    level = fields.Str(required=True)
    method = fields.Str(required=True)
    orthanc_id = fields.Str(required=False, data_key='orthanc-id')
    token_key = fields.Str(required=True, data_key='token-key')
    token_value = fields.Str(required=True, data_key='token-value')


class AuthResponseSchema(marshmallow.Schema):
    granted = fields.Bool()
    validity = fields.Int()
