from datetime import datetime, timedelta


def create_html(row):
    print(row)
    html_list = []
    html_list.append(row[0])
    if len(row) > 1:
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
    for i in range(0,9):
      row = []
      day_it = today - timedelta(days= i)
      row.append(day_it.strftime("%a, %b %d"))

      for day in resultset:
        if day_it == day[1]:
          row.extend(list(day[2:]))

      row = create_html(row)

      output.append(row)

    print(output)

    return output