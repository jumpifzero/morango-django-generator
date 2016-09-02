# ============================================================
# Tests for the DjangoGenerator class
#
# (C) Tiago Almeida 2016
#
# 
#
# ============================================================
import unittest
import DjangoGenerator
import morango.modelparser as modelparser
import morango.Models as Models

class TestModels(unittest.TestCase):
  def test_tests(self):
	  self.assertEqual(True, True)
  def test_blog_models_py_generation(self):
	  print('test_blog_models_py_generation')
	  # We instantiate the blog by using the parser
	  # so if the parser is incorrect, this will fail
	  models_raw = modelparser.parse_files(['test/blog.mdl'])
	  models = [Models.Model().init_from_parser(x) for x in models_raw]
	  generator = DjangoGenerator.DjangoGenerator(models)
	  models_py = generator._render_models()
	  print(models_py)
	  self.assertIsNotNone(models_py)

if __name__ == '__main__':
	unittest.main()