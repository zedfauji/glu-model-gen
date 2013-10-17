import os
import sys
import getopt



agent = [sys.argv[4]]
glu_template = open('templates/glu.template', 'r').read()
script="http://alp2.pv.sv.nextag.com:8080/glu/repository/scripts/sigiri/zed.groovy"
port=sys.argv[3]
service=sys.argv[1]
version=sys.argv[2]
output_dir="output"
mountPoint="/" +  service + "/p" +  port
def generate_glu(node_array):
	for agent in node_array:
		generate_host(agent, "glu", glu_template)

def generate_host(agent, type, template):
	print "GeneratingModel for Service %(service)s : %(agent)s" % {'agent': agent, 'service':service}
	output_file = open("%(output_dir)s/%(agent)s-%(service)s.json" % { "output_dir": output_dir, "agent":agent, "service": service}, "w")
	output_file.write(template % { "port" : port, "agent" : agent, "service": service, "version": version, "mountPoint": mountPoint,"script": script })
	output_file.close()

generate_glu(agent)


