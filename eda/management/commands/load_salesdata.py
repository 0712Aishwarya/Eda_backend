
# import pandas as pd
# from django.core.management.base import BaseCommand
# from eda.models import SalesData

# class Command(BaseCommand):
#     help = 'Load sales data from CSV'

#     def handle(self, *args, **kwargs):
#         # Load CSV
#         df = pd.read_csv(r'D:\EDA App\backend\data\sales.csv', encoding='utf-8-sig')
#         df.columns = df.columns.str.strip()  # Remove extra spaces

#         # Replace NaNs with safe defaults
#         df.fillna({
#             'Market': '',
#             'Channel': '',
#             'Region': '',
#             'Category': '',
#             'SubCategory': '',
#             'Brand': '',
#             'Variant': '',
#             'PackType': '',
#             'PPG': '',
#             'PackSize': '',
#             'Year': 0,
#             'Month': 0,
#             'Week': 0,
#             'BrCatId': '',
#             'SalesValue': 0,
#             'Volume': 0,
#             'VolumeUnits': 0,
#             'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0,
#             'AV1': 0, 'AV2': 0, 'AV3': 0, 'AV4': 0, 'AV5': 0, 'AV6': 0,
#             'EV1': 0, 'EV2': 0, 'EV3': 0, 'EV4': 0, 'EV5': 0, 'EV6': 0,
#             'date': ''
#         }, inplace=True)

#         # Clear existing data
#         SalesData.objects.all().delete()

#         sales_objects = []

#         for _, row in df.iterrows():
#             try:
#                 # Parse date (DD-MM-YYYY format)
#                 date_value = None
#                 if row['date']:
#                     try:
#                         date_value = pd.to_datetime(row['date'], dayfirst=True).date()
#                     except Exception:
#                         self.stdout.write(self.style.WARNING(f"Invalid date format in row: {row['date']}"))

#                 sales_objects.append(SalesData(
#                     market=row['Market'],
#                     channel=row['Channel'],
#                     region=row['Region'],
#                     category=row['Category'],
#                     sub_category=row['SubCategory'],
#                     brand=row['Brand'],
#                     variant=row['Variant'],
#                     pack_type=row['PackType'],
#                     ppg=row['PPG'],
#                     pack_size=row['PackSize'],
#                     year=int(row['Year']),
#                     month=int(row['Month']),
#                     week=int(row['Week']),
#                     date=date_value,
#                     brcat_id=row['BrCatId'],
#                     sales_value=row['SalesValue'],
#                     volume=row['Volume'],
#                     volume_units=row['VolumeUnits'],
#                     D1=row['D1'], D2=row['D2'], D3=row['D3'], D4=row['D4'], D5=row['D5'], D6=row['D6'],
#                     AV1=row['AV1'], AV2=row['AV2'], AV3=row['AV3'], AV4=row['AV4'], AV5=row['AV5'], AV6=row['AV6'],
#                     EV1=row['EV1'], EV2=row['EV2'], EV3=row['EV3'], EV4=row['EV4'], EV5=row['EV5'], EV6=row['EV6'],  
#                 ))
#             except Exception as e:
#                 self.stdout.write(self.style.WARNING(f"Skipping row due to error: {e}"))

#         if sales_objects:
#             SalesData.objects.bulk_create(sales_objects)

#         self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))

import pandas as pd
from django.core.management.base import BaseCommand
from eda.models import SalesData

class Command(BaseCommand):
    help = 'Load sales data from CSV, skipping completely blank rows'

    def handle(self, *args, **kwargs):
        # Load CSV
        df = pd.read_csv(r'D:\EDA_App\backend\data\sales.csv', encoding='utf-8-sig')
        df.columns = df.columns.str.strip()  # Remove extra spaces

        # Drop completely blank rows (where all values are NaN or empty)
        df.dropna(how='all', inplace=True)

        # Replace remaining NaNs with safe defaults
        df.fillna({
            'Market': '',
            'Channel': '',
            'Region': '',
            'Category': '',
            'SubCategory': '',
            'Brand': '',
            'Variant': '',
            'PackType': '',
            'PPG': '',
            'PackSize': '',
            'Year': 0,
            'Month': 0,
            'Week': 0,
            'BrCatId': '',
            'SalesValue': 0,
            'Volume': 0,
            'VolumeUnits': 0,
            'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0,
            'AV1': 0, 'AV2': 0, 'AV3': 0, 'AV4': 0, 'AV5': 0, 'AV6': 0,
            'EV1': 0, 'EV2': 0, 'EV3': 0, 'EV4': 0, 'EV5': 0, 'EV6': 0,
            'date': ''
        }, inplace=True)

        # Clear existing data
        SalesData.objects.all().delete()

        sales_objects = []

        for _, row in df.iterrows():
            try:
                # Skip completely blank rows (after stripping whitespace)
                if all((str(v).strip() == '' or pd.isna(v)) for v in row):
                    continue

                # Parse date (DD-MM-YYYY format)
                date_value = None
                if row['date']:
                    try:
                        date_value = pd.to_datetime(row['date'], dayfirst=True).date()
                    except Exception:
                        self.stdout.write(self.style.WARNING(f"Invalid date format in row: {row['date']}"))

                sales_objects.append(SalesData(
                    market=row['Market'],
                    channel=row['Channel'],
                    region=row['Region'],
                    category=row['Category'],
                    sub_category=row['SubCategory'],
                    brand=row['Brand'],
                    variant=row['Variant'],
                    pack_type=row['PackType'],
                    ppg=row['PPG'],
                    pack_size=row['PackSize'],
                    year=int(row['Year']),
                    month=int(row['Month']),
                    week=int(row['Week']),
                    date=date_value,
                    brcat_id=row['BrCatId'],
                    sales_value=row['SalesValue'],
                    volume=row['Volume'],
                    volume_units=row['VolumeUnits'],
                    D1=row['D1'], D2=row['D2'], D3=row['D3'], D4=row['D4'], D5=row['D5'], D6=row['D6'],
                    AV1=row['AV1'], AV2=row['AV2'], AV3=row['AV3'], AV4=row['AV4'], AV5=row['AV5'], AV6=row['AV6'],
                    EV1=row['EV1'], EV2=row['EV2'], EV3=row['EV3'], EV4=row['EV4'], EV5=row['EV5'], EV6=row['EV6'],
                ))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Skipping row due to error: {e}"))

        if sales_objects:
            SalesData.objects.bulk_create(sales_objects)

        self.stdout.write(self.style.SUCCESS(f'Data loaded successfully! Added {len(sales_objects)} records.'))
