import argparse
import anybadge
import xmltodict
import traceback

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--gen', choices=['pytest-cov'])
    parser.add_argument('--override-output-file')
    
    args = parser.parse_args()

    thresholds_cov =  {50 : 'red',
                       75 : 'orange',
                       90 : 'yellow',
                       100: 'green'}

    if args.gen=='pytest-cov':
        try:
            with open('coverage.xml', 'r') as f:
                cov = xmltodict.parse(f.read())
            cov_rate = float(cov['coverage']['@line-rate'])
            cov_rate = round(cov_rate*100)
            
            badge = anybadge.Badge(label='coverage', value=cov_rate, value_suffix='%', thresholds=thresholds_cov)
            badge.write_badge('coverage.svg', overwrite=args.override_output_file)
            
        except:
            traceback.print_exc()
    
if __name__ == '__main__':
    main()
