import csv
import os

class Top30CSVGenerator:

    def generate_top_30_csv(self, top_30_array, csv_file_location=os.path.expanduser('~/Downloads/'), file_name='ItJobsWatchTop30.csv', headers_array=None):
        with open(csv_file_location + file_name, 'w+') as top30csv:
            writer = csv.writer(top30csv)
            if headers_array is not None:
                writer.writerow(headers_array)
            writer.writerows(top_30_array)

            # if headers_array is not None:
            #     for i in headers_array:
            #         i.encode('utf-8')
            #         writer.writerow(headers_array)
            # for i in top_30_array:
            #     for j in i:
            #         j.encode('utf-8')
            #         writer.writerows(top_30_array)


if __name__ == '__main__':
    print()
