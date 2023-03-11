# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from paycomet_client.paths.v1_errors import Api

from paycomet_client.paths import PathValues

path = PathValues.V1_ERRORS