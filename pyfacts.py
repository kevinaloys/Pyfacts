#/usr/bin/python3
__author__ = 'Kevin Aloysius'
import re
import sys
class distribution:
		def __init__(self, **distro):
			infile = open('/etc/lsb-release','r')
			distribution_pattern = re.compile('DISTRIB_ID=([\w]+)\sDISTRIB_RELEASE=([\d]+.[\d]+)\sDISTRIB_CODENAME=([\w]+)\sDISTRIB_DESCRIPTION=\"(.+)\"')
			result = re.match(distribution_pattern, infile.read())
			distro = dict(distribution = result.group(1), release = result.group(2), codename = result.group(3).capitalize(), description = result.group(4))

			self.distro_facts = distro

		def get_fact(self, property):
			return self.distro_facts.get(property, 'No such facts')


		def all_distro_facts(self):
			for property, value in self.distro_facts.items():
				print(property.capitalize(),':',value)
		
def pyfacter(argv):
	distro = distribution()
	if sys.argv[1] == 'pyfacts':
		distro.all_distro_facts()
	elif sys.argv[1] == 'name':
		print(distro.get_fact('distribution'))
	elif sys.argv[1] == 'release':
		print(distro.get_fact('release'))
	elif sys.argv[1] == 'codename':
		print(distro.get_fact('codename'))
	elif sys.argv[1] == 'describe':
		print(distro.get_fact('description'))
if __name__ =='__main__':
	pyfacter(sys.argv)