from six import text_type

from ..language.ast import BooleanValue, FloatValue, IntValue, StringValue
from .definition import GraphQLScalarType

# Integers are only safe when between -(2^53 - 1) and 2^53 - 1 due to being
# encoded in JavaScript and represented in JSON as double-precision floating
# point numbers, as specified by IEEE 754.
MAX_INT = 9007199254740991
MIN_INT = -9007199254740991


def coerce_int(value):
    try:
        num = int(value)
    except ValueError:
        try:
            num = int(float(value))
        except ValueError:
            return None
    if MIN_INT <= num <= MAX_INT:
        return num
    return None


def parse_int_literal(ast):
    if isinstance(ast, IntValue):
        num = int(ast.value)
        if MIN_INT <= num <= MAX_INT:
            return num


GraphQLInt = GraphQLScalarType(
    name='Int',
    description='The `Int` scalar type represents non-fractional signed whole numeric '
                'values. Int can represent values between -(2^53 - 1) and 2^53 - 1 since '
                'represented in JSON as double-precision floating point numbers specified'
                'by [IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point).',
    serialize=coerce_int,
    parse_value=coerce_int,
    parse_literal=parse_int_literal)


def coerce_float(value):
    try:
        num = float(value)
    except ValueError:
        return None
    if num == num:  # is NaN?
        return num
    return None


def parse_float_literal(ast):
    if isinstance(ast, (FloatValue, IntValue)):
        return float(ast.value)
    return None


GraphQLFloat = GraphQLScalarType(
    name='Float',
    description='The `Float` scalar type represents signed double-precision fractional '
                'values as specified by '
                '[IEEE 754](http://en.wikipedia.org/wiki/IEEE_floating_point). ',
    serialize=coerce_float,
    parse_value=coerce_float,
    parse_literal=parse_float_literal)


def coerce_string(value):
    if isinstance(value, bool):
        return u'true' if value else u'false'

    return text_type(value)


def parse_string_literal(ast):
    if isinstance(ast, StringValue):
        return ast.value

    return None


GraphQLString = GraphQLScalarType(
    name='String',
    description='The `String` scalar type represents textual data, represented as UTF-8 '
                'character sequences. The String type is most often used by GraphQL to '
                'represent free-form human-readable text.',
    serialize=coerce_string,
    parse_value=coerce_string,
    parse_literal=parse_string_literal)


def parse_boolean_literal(ast):
    if isinstance(ast, BooleanValue):
        return ast.value
    return None


GraphQLBoolean = GraphQLScalarType(
    name='Boolean',
    description='The `Boolean` scalar type represents `true` or `false`.',
    serialize=bool,
    parse_value=bool,
    parse_literal=parse_boolean_literal)


def parse_id_literal(ast):
    if isinstance(ast, (StringValue, IntValue)):
        return ast.value
    return None


GraphQLID = GraphQLScalarType(
    name='ID',
    description='The `ID` scalar type represents a unique identifier, often used to '
                'refetch an object or as key for a cache. The ID type appears in a JSON '
                'response as a String; however, it is not intended to be human-readable. '
                'When expected as an input type, any string (such as `"4"`) or integer '
                '(such as `4`) input value will be accepted as an ID.',
    serialize=str,
    parse_value=str,
    parse_literal=parse_id_literal)
