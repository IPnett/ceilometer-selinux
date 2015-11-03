# ceilometer-selinux
SElinux policy for ceilometer

You probably need to label ports for this policy to work

Like this:

semanage port -a -t ceilometer_api_port_t -p tcp 8777
