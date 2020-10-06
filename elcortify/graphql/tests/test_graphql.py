import json

from graphene_django.utils import GraphQLTestCase

from elcortify.products.tests.factories import CategoryFactory, ProductFactory


class GQLTestCase(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"


class CategoryTestCase(GQLTestCase):
    def test_list_categories(self):
        categories = CategoryFactory.create_batch(size=8)
        op_name = "allCategories"
        fields = ["name"]
        response = self.query(
            """
            query {{
                {name} {{
                    edges {{
                        node {{
                            {fields}
                        }}
                    }}
                }}
            }}
            """.format(
                name=op_name, fields=" ".join(fields)
            ),
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(categories), len(content["data"][op_name]["edges"]))


class ProductTestCase(GQLTestCase):
    def test_list_products(self):
        products = ProductFactory.create_batch(size=8)
        op_name = "allProducts"
        fields = ["name", "price", "stock", "category { name }"]
        response = self.query(
            """
            query {{
                {name} {{
                    edges {{
                        node {{
                            {fields}
                        }}
                    }}
                }}
            }}
            """.format(
                name=op_name, fields=" ".join(fields)
            ),
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(products), len(content["data"][op_name]["edges"]))
