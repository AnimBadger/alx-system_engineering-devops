#kill a process called killmenow

exec { 'pkill':
  provider => 'shell',
  command  => 'pkill killmenow'
}
