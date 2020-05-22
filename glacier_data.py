# Important: fill the list with increasing rgi-ids!
# order of entries in tuples: 
                        # RGI-ID, Name, glacier type(Pure ice glacier, Debris covered glacier, Calving glacier, Ice cap),
                        # location from where picture is loaded into app,
                        # Photo courtesy text, license abbrevation, license link, 
                        # width image in hover, height image in hover, source link

glaciers = [('RGI60-01.01104', 'Lemon Creek Glacier', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/lemoncreek.jpg', 
               "Photo courtesy", "L. Bernier/National Snow and Ice Data Center",
               '', '',
               '390', '260',
              'http://nsidc.org/data/glacier_photo/search/image_info/lemoncreek20070917 '),
              
              ('RGI60-01.10689', 'Columbia Glacier', 'Calving glacier',
               'https://upload.wikimedia.org/wikipedia/commons/7/7b/Columbia_Glacier_%28Alaska%29_by_Sentinel-2.jpg', 
               "", 'Photo contains modified Copernicus Sentinel-2 data, (European Space Agency - ESA)  2018', 
               '(CC BY-SA 3.0 IGO)', 'https://creativecommons.org/licenses/by-sa/3.0/igo/deed.en',
               '300', '318',
              'https://commons.wikimedia.org/wiki/File:Columbia_Glacier_(Alaska)_by_Sentinel-2.jpg '),
             
              ('RGI60-03.04539', 'White Glacier', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/white.jpg',
               'Photo courtesy', 'J. Alean/National Snow and Ice Data Center',
               '', '',
               '300', '200', # this is set to very small outlines, otherwise it would be outside the margin of the browser window
              'http://nsidc.org/data/glacier_photo/search/image_info/white20080702'),
              
              ('RGI60-05.11186', 'Mittivakkat Glacier', 'Ice cap',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/mittivakkat.jpg', 
               'Photo courtesy', 'N. Knudsen/National Snow and Ice Data Center',
               '', '',
               '400', '300',
              'http://nsidc.org/data/glacier_photo/search/image_info/mittivakkat20130827?order=true '),
              
              ('RGI60-07.00570', 'Nordenskioldbreen', 'Calving glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/nordenskioldbreen.JPG', 
               'Photo courtesy', 'H. Crites',
               '', '',
               '300', '225', # this is set to very small outlines, otherwise it would be outside the margin of the browser window
              ''), # https://www.researchgate.net/publication/325218515_Drumlins_in_the_Nordenskioldbreen_forefield_Svalbard           
              
              ('RGI60-08.01097', 'Briksdalsbreen', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/briksdalsbreen.jpg',
               'Photo courtesy', 'J. Perez Crespo/National Snow and Ice Data Center',
               '(CC BY-NC)', '',
               '259', '387',
              'http://nsidc.org/data/glacier_photo/search/image_info/briksdalsbreen20090730?order=true'),
              
              ('RGI60-11.00897', 'Hintereisferner', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/hintereisferner.bmp', 
               'Photo courtesy', 'A. Lambrecht/National Snow and Ice Data Center',
               '', '',
               '400', '265',
              'http://nsidc.org/data/glacier_photo/search/image_info/hintereisferner20060912?order=true'), 
              
              ('RGI60-11.01450', 'Großer Aletschgletscher', 'Pure ice glacier',
               'https://upload.wikimedia.org/wikipedia/commons/a/a1/Grosser_Aletschgletscher_3196.JPG', 
               'Photo courtesy', 'Dirk Beyer',
               '(CC BY-SA 3.0)', 'https://creativecommons.org/licenses/by-sa/3.0/',
               '408', '306',
              'https://commons.wikimedia.org/wiki/File:Grosser_Aletschgletscher_3196.JPG'), 
              
              ('RGI60-12.00411', 'Tbilisa Glacier', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/tbilisa.jpg', 
               'Photo courtesy', 'L. Tielidze/National Snow and Ice Data Center',
               '', '',
               '360', '272',
              'http://nsidc.org/data/glacier_photo/search/image_info/tbilisa20109999'),
              
              ('RGI60-15.03733', 'Khumbu Glacier', 'Debris covered glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/khumbu.JPG', 
               'Photo courtesy', 'Z. Schirmeister',
               '', '',
               '400', '300',
              ''),

              ('RGI60-16.01638', 'Lewis', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/lewis.jpg', 
               'Photo courtesy', 'R. Prinz/National Snow and Ice Data Center',
               '', '',
               '400', '300',
              'http://nsidc.org/data/glacier_photo/search/image_info/lewis20120223'),
              
              ('RGI60-16.02444', 'Artesonraju', 'Pure ice glacier',
               'https://upload.wikimedia.org/wikipedia/commons/0/06/Artesonraju_Peru.jpg', 
               'Photo courtesy', 'Jonas Jancarik',
               '(CC BY 3.0)', 'https://creativecommons.org/licenses/by/3.0/deed.en',
               '400', '276',
              'https://commons.wikimedia.org/wiki/File:Artesonraju_Peru.jpg'), 
              
              ('RGI60-17.00312', 'Perito Moreno', 'Calving glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/peritomoreno.jpg', 
               '', 'Imagery from International Space Station, courtesy Earth Science and Remote Sensing Unit, NASA Johnson Space Center',
               '', '',
               '400', '272',
              'https://eol.jsc.nasa.gov/SearchPhotos/photo.pl?mission=ISS016&roll=E&frame=24897'),
              
              ('RGI60-18.02342', 'Tasman Glacier', 'Debris covered glacier',
               'https://upload.wikimedia.org/wikipedia/commons/8/87/Lower_Tasman_Glacier_towards_Minarets.jpg', 
               '', 
               '', '(released into public domain by holder of the work)', '',
               '400', '266',
              'https://commons.wikimedia.org/wiki/File:Lower_Tasman_Glacier_towards_Minarets.jpg '),
              
              ('RGI60-19.00595', 'Bahia Del Diablo Glacier', 'Pure ice glacier',
               'https://raw.githubusercontent.com/OGGM/glacier-gallery/master/glacier_photos/bahiadeldiablo.bmp', 
               'Photo courtesy', 'P. Skvarca/National Snow and Ice Data Center', 
               '', '',
               '400', '260',
              'http://nsidc.org/data/glacier_photo/search/image_info/bahiadeldiablo20040224')
             ]
# More glacier suggestions:
              #('RGI60-09.00114', 'Severny Island Ice Cap', np.NaN, np.NaN, '', ''),
              #('RGI60-09.00471', 'Vavilov Ice Cap', np.NaN, np.NaN,  '', ''),
              #('RGI60-13.04946', 'Samoilowich', np.NaN, np.NaN, '', ''), 
              #('RGI60-19.00386', 'Ross Island', '', '', ''),
                

links = {
    # links of the licences of the pictures
    'links_license': """<div> 
        <a href="https://creativecommons.org/licenses/by-sa/3.0/igo/deed.en">CC BY-SA 3.0 IGO </a> <br>
        <a href="https://creativecommons.org/licenses/by-nc/4.0/"> CC BY-NC</a> <br>
        <a href="https://creativecommons.org/licenses/by-sa/3.0/">CC BY-SA 3.0 </a> <br>
        <a href="https://creativecommons.org/licenses/by/3.0/deed.en">CC BY 3.0 (Creative Commons Attribution 3.0 Unported)</a>
                      </div>""",

    # links to the sources of the pictures
    'links_pics': """<div>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/lemoncreek20070917" >Lemon Creek Glacier</a> <br>
        <a href="https://commons.wikimedia.org/wiki/File:Columbia_Glacier_(Alaska)_by_Sentinel-2.jpg" >Columbia Glacier</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/white20080702?order=true" >White Glacier</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/mittivakkat20130827?order=true" > Mittivakkat Glacier</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/briksdalsbreen20090730?order=true" >Briksdalsbreen</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/hintereisferner20060912?order=true" >Hintereisferner</a> <br>
        <a href="https://commons.wikimedia.org/wiki/File:Grosser_Aletschgletscher_3196.JPG" >Großer Aletschgletscher</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/tbilisa20109999" >Tbilisa Glacier</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/lewis20120223" >Lewis Glacier</a> <br>
        <a href="https://commons.wikimedia.org/wiki/File:Artesonraju_Peru.jpg" >Artesonraju</a> <br>
        <a href="https://eol.jsc.nasa.gov/SearchPhotos/photo.pl?mission=ISS016&roll=E&frame=24897" >Perito Moreno</a> <br>
        <a href="https://commons.wikimedia.org/wiki/File:Lower_Tasman_Glacier_towards_Minarets.jpg" >Tasman Glacier</a> <br>
        <a href="http://nsidc.org/data/glacier_photo/search/image_info/bahiadeldiablo20040224" >Bahia Del Diablo Glacier</a>
                   </div>"""
}
