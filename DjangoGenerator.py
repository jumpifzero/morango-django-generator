# ============================================================
# modelparser.py
#
# (C) Tiago Almeida 2016
#
# Still in early development stages.
#
# ============================================================
import os
import random
import string
from jinja2 import Environment, FileSystemLoader
from subprocess import Popen, PIPE, STDOUT


def _render_field(f):
	"""
	For fields which are not basic types, 
	Receives a field and injects a 'rendered' property containing the
	django definition of the same field.
	"""
	if f.relationship:
		if f.multiplicity.max == 1:
			f.rendered = ( "models.ForeignKey('%s', blank=%s)" % 
				( f.type, f.multiplicity.min==0 ) )
		else:
			f.rendered = ( "models.ManyToManyField('%s', blank=%s)" % 
				( f.type, f.multiplicity.min==0 ) )
	return f


def _render_model_fields(m):
	"""
	Given a model, injects a rendered property on some of 
	its fields.
	"""
	m.fields = list(map(_render_field, m.fields))
	return m 	


class DjangoGenerator():

	class JinjaGenerator():
		def __init__(self):
			self.PATH = os.path.dirname(os.path.abspath(__file__))
			self.TEMPLATE_ENVIRONMENT = Environment(
		    autoescape=False,
		    loader=FileSystemLoader(
		    	os.path.join(self.PATH, 'data/DjangoGenerator')),
		    trim_blocks=True,
		    lstrip_blocks=True)
		#
		def render(self, template_filename, context):
			return (self.TEMPLATE_ENVIRONMENT
							.get_template(template_filename)
							.render(context))


	def __init__(self, models):
		"""
		DjangoGenerator constructor
		Initialize:
			- name of app
			- name of project
			- a jinja2 generator 
			- project base path
		"""
		self.app_name = 'webapp'
		self.prj_name = ''.join(
			random.choice(string.ascii_lowercase) for _ in range(6))
		self.prj_env_name= self.prj_name + '-env'
		self.base_path = os.getcwd()
		self.models = models
		self.text = {'generated_proj':'Generated project %s.'}
		self.generator = DjangoGenerator.JinjaGenerator()
		self.admin_email = 'a@b.com' #TODO (must come from outside)
		# Full list of dependencies that need to be installed
		self.dependencies = [ 
			'django',
			'git+https://github.com/jumpifzero/django-baker.git' 
		]
	#
	#
	def get_app_path(self):
		# TODO: join paths better
		return '%s/%s/%s' % (self.base_path, 
													self.prj_name, 
													self.app_name)
	#
	def get_proj_path(self):
		# TODO: join paths better
		return '%s/%s' % (self.base_path, 
											self.prj_name)
	#
	
	#
	#
	def _render_models(self):
		"""
		Given the current models definition,
		returns a rendered string of models.py.
		Because there is quite a bit of logic on
		how to convert these into a django model,
		I expect this function to grow and
		become a class on its own...
		"""
		# Related fields are complex, we do the logic here
		# and on the template we only print the generated string
		self.models = list(map(_render_model_fields, self.models))
		context = {
			'models': self.models
		}
		return self.generator.render('models.template.py', context)
	#
	#
	def generate_models(self):
		# TODO: join paths better
		fname = self.get_app_path() + "/models.py" 
		code = self._render_models()
		with open(fname, 'w') as f:
			f.write(code)
	
	#
	def generate_admin(self):
		app_path = self.get_app_path()
		fname = app_path + "/admin.py"
		assert (len(self.models) > 0)
		context = {
			'models': self.models
		}
		#
		with open(fname, 'w') as f:
			code = self.generator.render('admin.template.py', context)
			f.write(code)
	#
	def generate_settings(self):
		context = {
			'project_name': self.prj_name
		}
		code = self.generator.render('settings.template.py', context)
		proj_path = self.get_proj_path()
		fname = proj_path + "/%s/settings.py" % self.prj_name
		with open(fname, 'w') as f:
			f.write(code)
	#
	def set_admin_password(self):
		import os
		import sys
		import django

		sys.path.append("./") #path to your settings file  
		os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % self.prj_name
		print(os.environ['DJANGO_SETTINGS_MODULE'])
		print(sys.path)
		print(os.getcwd())
		django.setup()
		from django.contrib.auth.models import User
		u = User.objects.get(username__exact='admin')
		u.set_password('1234')
		u.save()
	#
	def go(self):
		# TODO: somewhat hacky code to fix later
		# TODO: Join paths better!
		# Create a virtualenv
		os.system('virtualenv %s' % self.prj_env_name )
		# Switch to it
		activate_this = os.path.join(self.prj_env_name,
			'bin', 'activate_this.py')
		with open(activate_this, 'r') as f:
			exec(f.read(), dict(__file__=activate_this))
		# Install all dependencies
		for dep in self.dependencies:
			os.system('pip install %s' % dep)
		# 
		os.system('django-admin startproject %s' % self.prj_name)
		os.chdir(self.prj_name)
		os.system('django-admin startapp %s' % self.app_name)
		self.generate_models()
		self.generate_admin()
		self.generate_settings()
		# TODO: python3
		os.system('python3 manage.py makemigrations')
		os.system('python3 manage.py migrate')
		os.system('python3 manage.py createsuperuser \
								--noinput --username admin --email %s' %
							(self.admin_email))
		print(self.text['generated_proj'] % self.prj_name)
		self.set_admin_password()
		# Generate templates with django_baker
		os.system('python3 manage.py bake webapp')
		# Write base.html file	
		# TODO
		os.chdir(self.prj_name)
		print(self.text['generated_proj'] % self.prj_name)
