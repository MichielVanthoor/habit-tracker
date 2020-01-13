from datetime import datetime, timedelta

def create_html(row):
    html_list = []

    # Add the date
    html_list.append(row[0].strftime("%a, %b %d"))

    # Add html if weekend day
    if row[0].weekday() >=5:
      html_list.append('info')
    else:
      html_list.append('')

    if len(row) > 2:
      # Detect 'snoozed'
      if row[1] == 0:
        html_list.append('warning')
      else:
        html_list.append('danger')

      # Detect 'water_drank'
      if row[6] == 1:
        html_list.append('warning')
      else:
        html_list.append('danger')

      # Detect 'teeth_brushed_am'
      if row[2] == 1:
        html_list.append('warning')
      else:
        html_list.append('danger')

      # Detect 'www_used_am'
      if row[4] == 0:
        html_list.append('warning')
      else:
        html_list.append('danger')

      # Detect 'teeth_brushed_pm'
      if row[3] == 1:
        html_list.append('warning')
      else:
        html_list.append('danger')

      # Detect 'www_used_pm'
      if row[5] == 0:
        html_list.append('warning')
      else:
        html_list.append('danger')

    return html_list

def generate_output(resultset):
    today = datetime.today().date()

    output = []
    for i in range(0,6):
      row = []
      day_it = today - timedelta(days= i)
      row.append(day_it)

      for day in resultset:
        if day_it == day[1]:
          row.extend(list(day[2:]))

      row = create_html(row)

      output.append(row)

    return output