love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = [ ]
value = None

for love in love_maybe_lines:
   value = love.strip()
   print(value)
   love_maybe_lines_stripped.append(value)

print(love_maybe_lines_stripped)