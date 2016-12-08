"""
Container for stations.

:copyright:
    Mazama Science
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""

from __future__ import (absolute_import, division, print_function)

import urllib

import numpy as np
import pandas as pd

class StationsHandler(object):
    """
    Container for stations.
    """
    def __init__(self, logger, preferences):
        """
        Initialization.
        """
        # Always keep a reference to global logger and preferences
        self.logger = logger
        self.preferences = preferences

        # Current state
        self.currentDF = None
        self.selectedIDs = []
        
    def load_data(self, parameters=None):
        """
        Make a webservice request for stations using the passed in options
        """
        # Sanity check
        if not parameters.has_key('starttime') or not parameters.has_key('endtime'):
            raise('starttime or endtime is missing')                   
        
        try:
            # Create dataframe of stations metadata
            url = build_url(parameters=parameters, output_format="text")
            self.logger.debug('Loading channels from: %s', url)
            df = build_dataframe(url)
            df = df[self.get_column_names()]
            
        except Exception as e:
            # TODO:  What type of exception should we trap? We should probably log it.
            self.logger.error('%s', e)
            raise

        self.currentDF = df

        return(df)
        
    def get_column_names(self):
        columnNames = ['Network', 'Station', 'Location', 'Channel', 'Longitude', 'Latitude', 'Elevation', 'Depth', 'Azimuth', 'Dip', 'SensorDescription', 'Scale', 'ScaleFreq', 'ScaleUnits', 'SampleRate', 'StartTime', 'EndTime', 'SNCL']
        return(columnNames)

    def get_selected_ids(self):
        return(self.selectedIDs)
    
    def set_selected_ids(self, IDs):
        self.selectedIDs = IDs
        
    def get_selected_dataframe(self):
        df = self.currentDF.loc[self.currentDF['SNCL'].isin(self.selectedIDs)]
        return(df)
    
        
# ------------------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------------------

# Similar to obspy.clients.fdsn.client.py
def build_url(base_url="http://service.iris.edu",
              service="station",
              major_version=1,
              resource_type="query",
              parameters={},
              output_format="xml"):
    """
    Build a FDSN webservice url to request stations.

    >>> print(build_url("http://service.iris.edu", "station", 1, \
                        "query", {'starttime':'2015-01-01','endtime':'2015-01-03','minmag':'4.00'}, "text"))
    http://service.iris.edu/fdsnws/station/1/query?endtime=2015-01-03&starttime=2015-01-01&minmag=4.00&format=text
    """

    # Construct base_url from FDSN provider, service, verstion.
    url = "/".join((base_url, "fdsnws", service,
                    str(major_version), resource_type))
    
    # Add parameter for channel-level output
    parameters['level'] = 'channel'
    
    # Aded a parameter for the output format -- either 'xml' (used to generate an ObsPy inventory) or 'text' (used to generate a pandas dataframe)
    parameters['format'] = output_format

    # Add parameters
    url = "?".join((url, urllib.urlencode(parameters)))
    
    return(url)


# build a stations dataframe (original IRIS version)
def build_dataframe(url):
    # Get stations dataframe and clean up column names
    df = pd.read_csv(url, sep='|')
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.strip('#')   # take care of column named '#Network'
    # Awkward conversion of 'Location' column from float to character
    # NOTE:  Using [:,'colname'] syntax here because of the following warning:
    # NOTE:  http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    df.loc[np.isnan(df['Location']),'Location'] = 999
    df.loc[:,'Location'] = df.loc[:,'Location'].astype(int)
    df.loc[:,'Location'] = df.loc[:,'Location'].astype(str)
    df.loc[df['Location'] == '999','Location'] = '--'          # Could be represented as '' or '--'
    df.loc[df['Location'] == '0','Location'] = '00'
    # Add 'SNCL' column
    sncls = df.apply(lambda x: '%s.%s.%s.%s' % (x['Network'],x['Station'],x['Location'],x['Channel']), axis=1)
    df['SNCL'] = sncls.tolist()
    
    return(df)
    

# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)
