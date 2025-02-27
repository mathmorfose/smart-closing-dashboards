import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Smart Closing Dashboards",
    layout="wide"
)
# Import your data
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")
 
st.title("Build your own Smart Closing Dashboard")
# pyg_html = pyg.walk(df, retur_html=True)
# components.html(pyg_html, height=10000)

vis_spec = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["auto"],"coordSystem":"generic","limit":-1,"timezoneDisplayOffset":0},"encodings":{"dimensions":[{"fid":"date","name":"date","basename":"date","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"month","name":"month","basename":"month","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"season","name":"season","basename":"season","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"year","name":"year","basename":"year","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"holiday","name":"holiday","basename":"holiday","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"work yes or not","name":"work yes or not","basename":"work yes or not","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"am or pm","name":"am or pm","basename":"am or pm","semanticType":"nominal","analyticType":"dimension","offset":0},{"fid":"Day of the week","name":"Day of the week","basename":"Day of the week","semanticType":"quantitative","analyticType":"dimension","offset":0},{"fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"fid":"hour","name":"hour","basename":"hour","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"temperature","name":"temperature","basename":"temperature","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"feeling_temp","name":"feeling_temp","basename":"feeling_temp","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"humidity","name":"humidity","basename":"humidity","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"winspeed","name":"winspeed","basename":"winspeed","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"casual","name":"casual","basename":"casual","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"registered","name":"registered","basename":"registered","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"count","name":"count","basename":"count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","offset":0},{"fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"fid":"season","name":"season","basename":"season","semanticType":"nominal","analyticType":"dimension","offset":0}],"columns":[{"fid":"temperature","name":"temperature","basename":"temperature","analyticType":"measure","semanticType":"quantitative","aggName":"median","offset":0}],"color":[],"opacity":[],"size":[],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"auto","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"gw_AkX-","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["season"],"measures":[{"field":"temperature","agg":"median","asFieldKey":"temperature_median"}]}]}]}],"version":"0.4.9.14"}"""


pyg_app = StreamlitRenderer(df, spec=vis_spec)
 
pyg_app.explorer()