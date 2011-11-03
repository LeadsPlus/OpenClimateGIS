import unittest
from ocg_dataset import OcgDataset
from shapely.geometry.point import Point
import ipdb
import datetime
from shapely import wkt


def convert_wkt(f):
    def wrapf(*args,**kwds):
        return(wkt.loads(f(*args,**kwds)))
    return(wrapf)


class Geometries(object):
    
    def simple_polygon(self):
        pt = Point(200,0.0)
        return(pt.buffer(8,1))
    
    @convert_wkt
    def nebraska(self):
        wkt = "POLYGON ((-101.407393290830782 40.001003364718585,-102.051535291430682 39.998918364716637,-102.047545291426971 40.342644365036762,-102.047620291427037 40.431077365119123,-102.046031291425564 40.697319365367079,-102.046992291426449 40.743130365409741,-102.047739291427149 40.998071365647171,-102.621257291961285 41.000214365649171,-102.652271291990161 40.998124365647222,-103.38295629267067 41.000316365649262,-103.57231629284702 40.999648365648639,-104.051705293293494 41.003211365651964,-104.054012293295642 41.388085366010401,-104.055500293297015 41.564222366174441,-104.053615293295266 41.69821836629923,-104.053513293295168 41.999815366580123,-104.056219293297687 42.614669367152743,-104.056199293297666 43.003062367514467,-103.501464292781037 42.998618367510332,-103.005875292319487 42.999354367511017,-102.78838429211693 42.99530336750724,-102.086701291463442 42.989887367502192,-101.231737290667184 42.986843367499361,-100.198142289704577 42.99109536750332,-99.532790289084915 42.992335367504474,-99.253971288825255 42.992389367504529,-98.497651288120878 42.991778367503954,-98.457444288083423 42.937160367453089,-98.39120428802174 42.920135367437233,-98.31033928794642 42.881794367401525,-98.167826287813696 42.839571367362204,-98.144869287792318 42.835794367358687,-98.123117287772061 42.820223367344184,-98.121820287770845 42.808360367333137,-98.033140287688255 42.769192367296654,-97.995144287652877 42.766812367294442,-97.963558287623457 42.773690367300844,-97.929477287591723 42.792324367318201,-97.88994128755489 42.831271367354475,-97.888659287553708 42.855807367377324,-97.818643287488499 42.866587367387368,-97.797028287468365 42.849597367371544,-97.772186287445223 42.846164367368345,-97.725250287401522 42.858008367379369,-97.685752287364735 42.836837367359657,-97.634970287317444 42.861285367382422,-97.57065428725754 42.847990367370045,-97.506132287197445 42.860136367381358,-97.483159287176051 42.857157367378576,-97.457263287151932 42.850443367372328,-97.389306287088644 42.867433367388152,-97.311414287016106 42.861771367382879,-97.271457286978887 42.850014367371926,-97.243189286952557 42.851826367373619,-97.224443286935099 42.841202367363721,-97.211831286923356 42.812573367337059,-97.161422286876416 42.798619367324065,-97.130469286847585 42.773923367301066,-97.01513928674018 42.759542367287665,-96.979593286707072 42.758313367286526,-96.970003286698145 42.752065367280707,-96.97786928670547 42.727308367257649,-96.970773286698858 42.721147367251916,-96.908234286640607 42.73169936726174,-96.810140286549256 42.704084367236021,-96.810437286549529 42.681341367214841,-96.799344286539196 42.67001936720429,-96.722658286467777 42.668592367202962,-96.6990602864458 42.657715367192836,-96.694596286441652 42.64116336717742,-96.715273286460899 42.621907367159487,-96.714059286459772 42.612302367150541,-96.636672286387693 42.550731367093199,-96.629294286380826 42.522693367067092,-96.605467286358632 42.507236367052691,-96.58475328633935 42.518287367062982,-96.547215286304393 42.520499367065042,-96.494701286255477 42.488459367035205,-96.439394286203964 42.489240367035933,-96.396074286163625 42.467401367015597,-96.397890286165321 42.441793366991746,-96.4176282861837 42.414777366966582,-96.411761286178233 42.380918366935049,-96.424175286189794 42.349279366905584,-96.389781286157771 42.328789366886497,-96.368700286138136 42.298023366857848,-96.342881286114078 42.282081366843002,-96.332658286104561 42.260307366822722,-96.337708286109262 42.22952236679405,-96.3635122861333 42.214042366779637,-96.352165286122727 42.168185366736921,-96.285123286060298 42.123452366695261,-96.265483286041999 42.04889736662583,-96.238725286017086 42.028438366606778,-96.236093286014636 42.001258366581467,-96.202842285983664 41.996615366577139,-96.185217285967255 41.980685366562298,-96.147328285931962 41.966254366548867,-96.145870285930599 41.924907366510354,-96.159970285943743 41.904151366491021,-96.135623285921056 41.862620366452347,-96.076417285865915 41.791469366386082,-96.099321285887257 41.752975366350228,-96.09977128588767 41.731563366330292,-96.08555728587443 41.704987366305538,-96.122202285908557 41.694913366296156,-96.120264285906757 41.684094366286082,-96.099306285887238 41.654680366258688,-96.11130728589842 41.599006366206837,-96.080835285870037 41.576000366185411,-96.091936285880379 41.563145366173437,-96.085840285874696 41.537522366149574,-96.050172285841484 41.524335366137294,-96.004592285799035 41.536663366148773,-95.99396528578913 41.528103366140805,-95.996688285791663 41.511517366125361,-96.013451285807278 41.492994366108107,-96.006897285801173 41.481954366097824,-95.953185285751147 41.47238736608891,-95.935065285734282 41.462381366079597,-95.940056285738919 41.394805366016655,-95.942895285741571 41.340077365965691,-95.88910728569148 41.301389365929658,-95.897591285699377 41.286863365916133,-95.911202285712051 41.308469365936254,-95.930230285729778 41.302056365930284,-95.910981285711841 41.22524536585874,-95.922250285722342 41.20785436584255,-95.91610028571661 41.194063365829706,-95.859198285663624 41.180537365817102,-95.859801285664176 41.16686536580437,-95.876685285679912 41.164202365801899,-95.858274285662759 41.109187365750657,-95.878804285681881 41.065871365710315,-95.859539285663942 41.035002365681564,-95.860897285665203 41.002650365651434,-95.83760328564351 40.974258365624991,-95.836541285642525 40.901108365556865,-95.834396285640523 40.87030036552818,-95.846435285651737 40.848332365507716,-95.851790285656719 40.792600365455812,-95.876616285679845 40.730436365397921,-95.767999285578682 40.643117365316598,-95.757546285568949 40.620904365295907,-95.767479285578204 40.589048365266237,-95.763412285574418 40.549707365229601,-95.737036285549848 40.532373365213459,-95.692066285507963 40.524129365205781,-95.687413285503638 40.561170365240272,-95.675693285492713 40.565835365244624,-95.662944285480847 40.558729365238008,-95.658060285476296 40.530332365211557,-95.684970285501365 40.512205365194674,-95.695361285511041 40.485338365169653,-95.636817285456516 40.396390365086816,-95.634185285454066 40.358800365051806,-95.616201285437313 40.346497365040349,-95.617933285438923 40.331418365026302,-95.645553285464644 40.32234636501785,-95.646827285465832 40.309109365005526,-95.595532285418059 40.309776365006144,-95.547137285372997 40.266215364965575,-95.476822285307506 40.226855364928923,-95.466636285298023 40.21325536491625,-95.46095228529272 40.173995364879687,-95.422476285256892 40.131743364840347,-95.392813285229266 40.115416364825137,-95.384542285221556 40.095362364806462,-95.403784285239482 40.080379364792506,-95.413764285248774 40.048111364762448,-95.390532285227138 40.043750364758395,-95.371244285209173 40.028751364744423,-95.345067285184797 40.024974364740906,-95.308697285150927 39.999407364717094,-95.329701285170486 39.992595364710752,-95.780700285590513 39.993489364711579,-96.001253285795926 39.995159364713139,-96.240598286018823 39.994503364712529,-96.45403828621761 39.994172364712213,-96.801420286541131 39.994476364712497,-96.908287286640657 39.996154364714066,-97.361912287063134 39.997380364715205,-97.816589287486579 39.999729364717396,-97.929588287591827 39.998452364716201,-98.264165287903424 39.998434364716189,-98.504479288127229 39.997129364714972,-98.720632288328545 39.998461364716213,-99.064747288649016 39.998338364716098,-99.178201288754678 39.999577364717254,-99.627859289173458 40.002987364720425,-100.180910289688526 40.000478364718091,-100.191111289698028 40.000585364718191,-100.735049290204614 39.99917236471687,-100.75485629022306 40.000198364717832,-101.322148290751386 40.001821364719341,-101.407393290830782 40.001003364718585))"
        return(wkt)


class TestOcgDataset(unittest.TestCase):
#    nc_path = '/home/bkoziol/git/OpenClimateGIS/bin/climate_data/wcrp_cmip3/pcmdi.ipcc4.bccr_bcm2_0.1pctto2x.run1.monthly.cl_A1_1.nc'
#    nc_opts = dict(rowbnds_name='lat_bnds',
#                   colbnds_name='lon_bnds',
#                   calendar='gregorian',
#                   time_units='days since 1800-1-1 00:00:0.0',
#                   level_name='lev')
    
    nc_path = '/home/bkoziol/git/OpenClimateGIS/bin/climate_data/maurer/bccr_bcm2_0.1.sresa2.monthly.Prcp.1951.nc'
    nc_opts = dict(rowbnds_name='bounds_latitude',
                   colbnds_name='bounds_longitude',
                   calendar='proleptic_gregorian',
                   time_units='days since 1950-01-01 00:00:0.0')
    
    _od = None
    _geoms = Geometries()
    
    @property
    def od(self):
        return(OcgDataset(self.nc_path,**self.nc_opts))

    def test_constructor(self):
        self.assertEqual(self.od.res,2.8125)
        
    def test_subset(self):
        polygon = self._geoms.simple_polygon()
        
        ## three time periods. two levels.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,12,31)],
                             level_range=[1,2])
        
        ## one time periods. one level.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,10,31)],
                             level_range=[1,1])

        ## one time periods. two levels.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,10,31)],
                             level_range=[1,2])
        
        ## one time period. no levels.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,10,31)])

        ## three time periods. no levels.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,12,31)])

#        sub.display(overlays=[polygon])

    def test_subset_clip(self):
        polygon = self._geoms.simple_polygon()
        
        ## three time periods. two levels.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,12,31)],
                             level_range=[1,2])
        sub.clip(polygon)
        self.assertTrue((sub.weight < 1.0).any())
#        ipdb.set_trace()
#        sub.display(overlays=[polygon])

    def test_subset_union(self):
        polygon = self._geoms.simple_polygon()
        
        ## three time periods. two levels.
        sub = self.od.subset('cl',
                             polygon=polygon,
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,12,31)],
                             level_range=[1,2])
        sub.clip(polygon)
        sub.union()
#        ipdb.set_trace()
        sub.display(overlays=[polygon])
        
    def test_motherlode(self):
        sub = self.od.subset('ps',
                             time_range=[datetime.datetime(2000,10,1),datetime.datetime(2000,10,31)])
#        sub.display()
#        ipdb.set_trace()

    def test_mapped_subset(self):
        polygon = self._geoms.simple_polygon()
        max_proc = 2
        union = True
        
        subset_opts = dict(polygon=polygon,
                           time_range=[datetime.datetime(2000,10,1),
                                       datetime.datetime(2000,10,31)])
        subs = self.od.mapped_subset('cl',max_proc=max_proc,subset_opts=subset_opts)
        self.od.parallel_process_subsets(subs,
                                         max_proc=max_proc,
                                         polygon=polygon,
                                         clip=True,
                                         union=union)
        psub = self.od.combine_subsets(subs,union=union)
        
    def test_nebraska(self):
        ne = self._geoms.nebraska()
#        self.od.display(overlays=[ne])
        sub = self.od.subset('Prcp',
                             polygon=ne,
                             time_range=[datetime.datetime(1951,1,1),datetime.datetime(1951,12,31)])
        sub.display(overlays=[ne])
        sub.clip(ne)
        sub.display(overlays=[ne])
        sub.union()
        sub.display(overlays=[ne])
        ipdb.set_trace()
        
    def test_nebraska_multiprocess(self):
        import time
        
        union = True
        clip = False
        polygon = self._geoms.nebraska()
        time_range = [datetime.datetime(1951,1,1),
                      datetime.datetime(1951,12,31)]
        var_name = 'Prcp'
        
        t1 = time.time()
        subset_opts = dict(time_range=time_range)
        subs = self.od.mapped_subset(var_name,max_proc=8,subset_opts=subset_opts)
        subs = self.od.parallel_process_subsets(subs,clip=clip,union=union)
        psub = self.od.combine_subsets(subs,union=union)
        t2 = time.time()
        print(t2-t1)
        
#        t1 = time.time()
#        asub = self.od.subset(var_name,time_range=time_range)
#        if clip:
#            asub.clip(polygon)
#        if union:
#            asub.union()
#        t2 = time.time()
#        print(t2-t1)
        
        ipdb.set_trace()

if __name__ == "__main__":
    import sys;sys.argv = ['', 'TestOcgDataset.test_nebraska_multiprocess']
    unittest.main()