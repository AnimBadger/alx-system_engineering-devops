#!/usr/bin/pup 
# install flask with specific version

package{'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
