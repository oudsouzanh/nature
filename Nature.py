import win32service
import win32serviceutil
import servicemanager
import win32api
import win32event
import sys
import socket
import os
import winreg
import urllib

aline=['adultcash.com', 'premiumhdv.com', 'olduvsen.cz', 'cumpleaser.com', 'passion.com', 'latinovirgin.com', 'moviedollars.com', 'shemalepepper.com', 'exgfsbucks.com', 'basal.ca', 'lovevoodoo.com', 'annavirgin.com', 'clubseventeen.com', 'freejpgseries.com', 'mofos.com', 'wankerhut.com', '3xtraffic.com', 'dancingbear.com', 'carpediem.fr', 'natursekt.tv', 'ehho.com', 'fooxy.com', 'rashatemraa.com', 'dreammovies.com', 'zbiornik.com', 'virginbody.com', 'hornywife.com', 'blogbang.com', 'thumbsweek.com', 'runawayangels.com', 'angelinajolie.nl', 'allsexblogs.com', 'tblop.com', 'cafedeangel.net', 'tv69.com', 'sheisangel.com', 'imlive.com', 'teenhost.net', 'newwebmaster.net', 'fantasy4you.info', 'glxgroup.com', 'camshunt.com', 'blondexxxmag.com', 'xxx.com', 'fuckvideo.org', 'phoneangels.com', 'fncash.com', 'helltraffic.com', 'angelelle.com', 'adultscandy.com', 'asktiava.com', 'bestangels.de', 'homo6.com', 'realvirgin.com', 'annangel.net', 'hqtube.com', 'luckyvirginz.com', 'tgptraffic.biz', 'digitaldesire.com', 'saharanights.info', 'porn8.com', 'celebritywar.com', 'legendarylars.com', 'cyberangels.org', 'topsexart.com', 'azkempire.com', 'adultadworld.com', 'joesvirgins.com', 'virginsmania.com', 'juiceadv.com', 'tuccus.com', 'tranent.nl', 'virgincards.com', 'alsscanangels.com', 'xxxbannerswap.com', 'sexsearchtgp.com', 'sexfg.com', 'icoonet.com', 'chatischat.com', 'monliveshow.com', 'attractivesex.com', 'sweetangel.tv', 'cutegurlz.com', 'virgins.info', '3at3ot.com', 'lubeyourtube.com', 'chinmaster.com', 'yobtdvd.com', 'cryangel.com', 'gangbanganal.com', 'virginsclub.net', 'feralsex.com', 'arenaporno.com', 'penix.fr', 'virginsbbs.com', 'smrd7.net', 'pornhublive.com', 'alexisvirgin.com', 'inaturist.com', 'virginopener.com', 'freeatkgals.com', 'thirdmovies.com', 'angelaandrews.com', 'sexybunnylove.com', 'oldpornsite.com', 'sboob.com', 'pinaccesscode.com', 'moviemix.net', 'arrobapay.com', 'antivirgins.com', 'hornbunny.com', 'fuckinsilly.com', 'redtube.com', 'wildxangel.com', 'virgingalactic.ca', 'homexfiles.com', 'theporn1.com', 'lostvirgin.com', 'virginz.net', 'asstraffic.com', 'adultcomix.biz', 'cumforcover.com', 'wank.net', 'kissteenclub.com', 'netphuck.com', 'icoodvd.com', 'fux.com', 'plumpchicks.net', 'virginplace.com', 'teensondicks.com', 'angelshot.net', 'angelarchives.com', 'tinaangel.com', 'angeldust24.com', 'latinexposure.com', 'amamilfs.com', 'buckangel.nl', 'onegranny.com', 'playmymovie.com', 'latexangel.com', 'fuxybabes.com', 'angelcream.com', 'japanxangels.com', 'myblackangels.com', 'angelagrant.com', 'virginass.com', 'allgaybdsm.com', 'ndcontent.com', 'b44.com', 'angelinaashe.com', 'jpangels.com', 'bigtitangels.com', 'devirginized.com', 'dickievirgin.org', 'billpics.com', 'allvirgins.com', 'shemalebot.com', 'xtoplist.com', '2virgins.com', 'eroticdisney.com', 'mirangelov.com', 'moviebox.com', 'planetsuzy.org', 'virgins19.com', 'pussybabes.net', 'amateuralbum.net', 'eveangel.com', 'tubepornteen.com', 'hotchyx.com', 'evaangel.net', 'sexzoznamka.eu', 'virgins.org', 'prettyvirgins.com', 'figaitaliana.com', 'mofonetwork.net', 'evaangelina.org', 'cashlayer.com', 'porn.org', 'allisonangel.com', 'enjoyangels.com', 'imagechan.com', 'humoron.com', 'sotransexuais.com', 'citysex.com', 'virginriver.com', 'sologirlguide.com', 'natursekt.de', 'oxcash.com', 'fattyangels.com', 'truecash.com', 'adameve.com', 'fatangel.com', 'primebreasts.net', 'porn.hu', 'virginslits.com', 'korriangel.com', 'angelveil.org', 'verbalangels.com', 'cliphunter.com', 'dacash.com', 'flashybabes.com', 'bdsmtheory.com', 'gonorar.com', 'ethnicangel.com', 'fuckervids.com', 'misguidedangel.nu', 'topfreaks.com', 'slavecomics.com', 'puredee.com', 'secretlittle.com', 'hardanime.com', 'mirrorgirls.com', 'videosz.com', 'pinkytoy.com', 'creamgoodies.com', 'onlyankara.com', 'sexdisney.com', 'ccgals.com', 'crazydumper.com', 'freexxxpages.net', 'evilangelcash.com', 'angelsofnight.com', 'hungangels.com', 'angelinaamour.com', 'thickbbwforum.com', 'rudefuck.com', 'grannyangel.com', '3redangels.com', 'groupandsex.com', 'camsangels.com', 'angelasavage.com', 'classyangel.com', 'angelinalove.net', 'angelicablack.net', 'anawjarrate.info', 'wetvirgins.com', 'wetangels.com', 'titflicks.com', 'seemygf.com', 'eminotobursa.com', 'dancefox.net', 'rnosh.com', 'indianangels.net', 'hardxtc.com', 'adultdatelink.com', 'angelchic.com', 'virgindot.com', 'virgintwat.com', 'angeltel.net', 'sexole.com', 'virginsadist.com', 'angeloflondon.com', 'lovenylons.com', 'sensexion.com', 'japanangels.com', 'easypic.com', 'captiveangels.com', 'tsdreamangel.com', 'mynakedweb.com', 'jizzboat.com', 'teenshorde.com', 'animediablo.com', 'alfamina.com', 'blogbugs.org', 'sexsearch.com', 'hardnstraight.com', 'xxxcupid.com', 'clamsangels.com', 'justusboys.net', 'teenscoreclub.com', 'angelass.com', 'desktopangels.net', 'annangel.com', 'eveangel.us', 'usercash.com', 'getbigvids.com', 'itsgonnahurt.com', 'assangels.com', 'hardwayout.com', 'themeetlocal.com', 'sapphicangels.com', 'angelscasting.net', 'karupsbabes.com', 'darkangellair.com', 'virtuagirlhd.com', 'porn.com', 'kaskoos.com', 'keezlive.com', 'utherverse.com', 'pornaccess.com', 'creoads.com', 'mellowvirgins.com', 'frauenhasser.info', 'cam4.com', 'virginriches.com', 'tophomevideos.com', 'estudiosexual.com', 'streamsex.com', 'celebsking.com', 'grayvee.com', 'primeskype.com', '4affiliate.net', '19angels.net', 'favouritecash.com', 'yobthd.com', 'linkfame.com', 'arkhangelskiy.com', 'sexcount.de', 'fastsexdate.com', 'archangels.ws', 'rejalsgays.info', 'awmads.com', 'erotizer.info', 'sugarangels.com', 'topadult10.com', 'sexangels.net', 'badvirgin.com', 'amsterdamned.com', 'indapool.com', 'wikiangela.com', 'watchmygf.com', 'freshxxxclips.com', 'chunkytgp.net', 'alsangels.com', 'yalladownload.com', '2bigtobetrue.com', 'webcamtop100.com', 'xyztraffic.com', 'virginsexx.com', 'seducedangel.com', 'angelbust.com', 'cocogals.com', 'virgintemple.com', 'angelclub.cz', 'cuteteenvideo.com', 'virginfilms.com', 'outinpublic.com', 'virginsvids.com', 'angelinaashe.net', 'onmpeg.com', 'brunetteangel.com', 'lookformilf.com', 'lookordie.com', 'eroxia.com', 'sexcounter.com', 'xlogz.com', 'evilangel.fr', 'hotmalepics.com', 'nightangel.com', 'blowingkisses.net', 'awempire.com', 'vickyvirgin.com', 'kidzilla.info', 'mdnhinc.com', 'pussy.org', 'angelbutton.com', 'cinemaden.com', 'pleasurecage.info', 'blogangela.com', 'pussyharem.com', 'eztzvuzvuz.info', 'sandralatina.com', 'britishcoeds.com', 'moonangelcash.com', 'fisgonclub.com', 'girlsgonewild.com', '3angelsvideo.com', 'psbbanners.com', 'krissylove.com', 'agnesangel.com', 'toppornblogs.com', 'bignaturals.com', 'cheekybanners.com', 'taxindecente.com', 'advertx.net', 'livecams.nl', 'yoslut.com', 'tnaflix.com', 'nnangels.com', 'voyeurweb.com', 'alsscan.com', 'angela2000.de', 'persianwomen.info', 'hotmomfree.com', 'orgiasreales.com', 'usualgirls.com', 'angelmovies.com', 'cheapadultdvd.com', 's7lob.com', 'angelmodel.info', 'nadiavirgin.net', 'hardtv.com', 'honeyvirgins.com', 'crazyshit.com', 'oldpichunter.com', 'natur.nl', 'alisonangel.fr', 'efukt.com', 'hornyspots.com', 'virginkitty.com', 'adultlinksco.com', 'atkpussies.com', 'virginhaven.com', 'pussy.com', 'moviezentral.com', 'burningangel.com', 'perfectangels.org', 'angelasummers.com', 'saraangell.com', 'eveangel.hu', 'spankwire.com', 'drunkporn.us', 'russianangels.com', 'angela21.com', 'xhamster.com', 'clubvirgins.com', 'hentailisting.com', 'virginsblog.com', 'nichearena.com', 'porn.xxx', 'dan81.com', 'flavinha.com', 'cynicalangel.com', 'hotelmgp.com', 'ass1st.com', 'purepov.com', 'movieaccess.com', 'flirt4free.com', 'virtuangels.com', 'za3ror.com', 'admost.nl', 'heaven666.org', '3virgin.com', 'blackvirgins.com', '3sex.com', 'angelheat.com', 'mostplays.com', 'angelie.com', 'dnvideos.com', 'brazilvirgin.com', 'suicideangel.com', 'zoosextv.com', 'cfnmidol.com', 'assvirgin.com', 'kontaktbox.de', 'affairsclub.com', 'hentaiseeker.com', 'beachtoplist.com', 'ucgalleries.com', 'zhirok.com', 'picladies.com', 'hushpass.com', 'glamourmilf.com', 'angelsofwar.nl', 'asianparade.com', 'erodynamics.nl', 'searchxfind.com', 'tinychat.com', 'exwifesexbook.com', 'trampararam.net', 'iwantu.com', 'livejasmin.tv', 'dangelopalace.com', 'angeladevi.com', 'yobt.tv', 'allinternal.com', 'naomiangel.com', 'porntracker.com', 'camelstyle.net', 'yourlustmedia.com', 'netplayground.com', 'teens24h.com', 'xvirgins.com', 'hqpornweb.com', 'clitgames.com', 'buckangelvod.com', 'blogtur.com', '5starangels.com', 'fallenvirgin.com', 'worldsex.com', 'pornvideos.com', 'bdsmxxxmovies.com', 'sexyoung.us', 'hardwomen.com', 'virginshack.com', 'rasazrak.info', 'freshangel.com', 'avatarcash.com', 'hsvirgins.com', 'seavirgin.com', 'twatgod.com', 'watchmynewgf.com', 'gfrevenge.com', 'pinkbabes.net', 'dirty101.com', 'xxxbunker.com', 'nyloner.com', 'assvirgins.net', 'bdsmpichunter.com', 'silkyangels.com', 'langelul.nl', 'angelitas.net', 'alisonangel.at', 'neovirgins.com', 'baltictop.com', 'oneshemale.com', 'fbbtop100.com', 'bannerout.com', 'angelicales.com', 'strangeland.net', 'camworld.nl', 'commetvidsnow.com', 'alsangel.com', 'evaangelina.fr', 'easysexdate.com', 'xpornking.com', 'spunkysheets.com', 'bloodyvirgin.com', 'barevirgins.com', 'netvirgin.com', 'hotdamnsam.com', 'naturistville.com', 'facebook.bi', 's7lob.net', 'xponsor.com', 'porn2.com', 'virgin50.com', 'latexangelic.com', 'bignatural.ws', 'thefreenude.com', 'spankbang', 'dirtylesbo.com', 'fatchickens.net', 'blueangel.nl', 'adressesx.com', 'chicashumedas.com', 'netnet50.com', 'cartoontube.com', 'angelika.net', 'nextpic.com', 'angelslinks.org', 'amateurfarm.net', 'virginpalace.de', 'chunkyangels.com', 'pacinocash.com', 'zoodollars.com', 'angelstpg.com', 'dvangels.com', 'boysfood.com', 'notarangelo.com', 'xdating.com', 'erinvirgin.com', 'skypesex.ru', 'angeleyes.ca', 'sultanswomen.com', 'toonaddict.com', 'bookofsex.com', 'protizer.net', 'fuckherass.net', 'aziangals.com', 'hazehim.com', 'ftvblog.info', 'primecups.com', 'moronisangels.com', 'myadultguide.net', 'banduraangels.com', 'cashangel.de', 'babezblog.com', 'humoronline.com', 'jennavirgin.com', 'pornorama.com', 'celebtaboo.com', 'fuckstarts.net', 'alcuda.com', 'gbcash.com', 'apornmovie.com', 'shopgiggles.com', 'teensforcash.com', 'joyangeles.com', 'ronsangels.com', 'joannaangel.com', 'youho.com', 'teenburg.com', 'evaangelina.ws', 'angelikaminsk.com', 'pufisi.com', 'dickievirgin.com', 'virginfriend.info', 'angelsmist.com', 'brazilvirgina.com', 'hyperku.info', 'perfect10.com', 'socalmovies.com', 'srandel.com', 'silkangels.com', 'topadult.ro', 'animalrating.com', 'moregonzo.com', 'yetisblog.com', 'strangeland.org', 'curvyangel.com', 'burningcamel.com', 'naturistcamp.com', 'abrutis.com', 'sweetkrissy.com', 'beerandshots.com', 'zloeradio.net', 'dailybasis.com', 'maturehills.com', 'elangelito.com', 'pimproll.com', 'elegantangel.com', 'amateurdevils.com', 'angelwoods.com', 'femdomworld.com', '40best.com', 'virginhood.com', 'cybererotica.com', 'pertunda.com', 'sensualwriter.com', 'gaytube.com', 'virginz.info', 'outpersonals.com', 'angellsummers.com', 'watchmygf.net', 'tightteela.com', 'videoangels.com', 'sexinyourcity.com', '4tube.com', 'entensity.net', 'natursektweb.de', 'xnxx.com', 'aebn.net', 'cumridden.com', 'footjobdiary.com', 'virginsnack.com', 'shinyangels.com', 'trafficholder.com', 'motel69.com', 'mixx.com', 'dirtyfinder.com', 'angelmode.com', 'angelalittle.net', 'sexcess.net', 'pornhost.com', 'blondangel.de', 'shyvirgin.net', 'streamen.com', 'popander.mobi', 'yesmessenger.com', 'virginsrus.com', 'youpornmate.com', 'carlhardwick.com', 'alt.com', 'veryvirgin.com', 'indianpharma.info', 'maniacpass.com', 'camelmedia.net', 'javhq.net', 'sweetdiscreet.com', 'usearchx.com', 'seoprofit.biz', 'cumshotscenes.com', 'angelsfire.nl', '3thehardway.nl', 'burningangel.net', 'footfootage.com', 'sexmoney.com', 'devirginize.com', 'ninavirgin.com', 's3xads.com', 'camz.com', 'angelinacrow.net', 'adxpansion.com', 'bignaturals.de', 'shemalemovies.us', 'alisonangel.cc', 'angelcrack.com', 'angeldesign.org', 'totalexposure.com', 'sweetvirgins.com', 'angelbodywear.com', 'destinyangel.net', 'juicyads.com', 'virginphoto.com', 'animal6.net', 'autolinkweb.com', 'allisonangel.info', 'italiahard.it', 'oyundas.org', 'jigolojigola.net', 'smutbdsm.com', 'assvirgins.com', 'assdumper.com', 'az7t1.com', 'fatbackmedia.com', 'videos2stars.com', 'ns4w.org', 'nylonclit.com', 'tokyoangels.com', 'plumpteens.net', 'nudesonline.com', 'worthymoms.com', 'hardcartoon.com', '1adult.com', 'latinavirgins.com', 'hotsologirlz.net', 'rusangels.net', 'filestube.com', 'allfordrocher.com', 'menssexguide.com', 'streamate.com', 'lesanal.com', 'virginx.com', 'penisbot.com', 'purefaces.com', 'angelcassidey.com', 'purefuck.com', 'dilf.com', 'poseparty.com', 'linksexchange.net', 'collegerules.com', 'evilangel.com', 'harddaddy.com', 'angelstolove.com', 'milkyangels.com', '100200film.com', 'plumpersworld.com', 'hornypharaoh.com', 'whatpornsite.com', 'loveshack.org', 'arabvirgin.com', 'playboy.com', 'topmomvideos.com', 'natursekt.nl', 'annangel.org', 'moviefreaker.com', 'jerk2it.com', 'jessicavirgin.com', 'xhit.com', 'camzter.com', 'metangels.com', 'hugetraffic.com', 'angelsweb.nl', 'teenssites.net', 'nfsx.com', 'visodangelo.com', 'hardfreshmen.com', 'playblog.org', 'herfirstdv.biz', 'nsgalleries.com', 'blackandshiny.com', 'amourangels.eu', 'blondangels.de', 'asso69110.org', 'youngandready.com', 'natursekt1a.net', 'redangel.hu', 'hoseangel.com', 'realfatgirls.net', 'bestarabtube.com', 'bustyvixen.net', 'jgalz.net', 'hotstunners.com', 'cumswap.net', 'takezoo.com', 'angelsofindia.com', 'dinathumbs.com', 'triplexposure.com', 'wetvirgin.net', 'celebflix.us', 'playboy.bg', 'pornattitude.com', 'movies4adults.com', 'damnage.com', 'fuckteenpussy.net', 'sextronix.com', 'virgins4free.com', 'virginoff.info', 'tightangels.com', 'piradinhas.com', 'banditmovies.com', 'carumbas.com', 'videosexperts.com', 'naturistbeach.com', 'angelkiss.jp', 'monkeycock.net', 'photovirgins.com', 'gayhitlist.com', 'nextdoornikki.com', 'virginseries.com', 'kos3araby.com', 'adultads.biz', 'xvideos.com', 'annasassets.com', 'angelascloset.com', 'laylasa5en.info', 'evasiveangels.com', 'akibaangels.com', 'groovybus.com', 'blowingangels.com', 'natursektweb.com', 'virginsuicide.com', 'angelina.de', 'sexpeeper.com', 'almostvirgins.com', 'hardassed.com', 'angelbutton.info', 'shelbyvirgin.com', 'myiplayground.com', '1virgins.net', 'strangewishes.com', 'xxxylive.com', 'sexmaxx.com', 'cash4members.com', 'arhangelsk.name', '18eighteenz.com', 'teenfunzone.com', '6eez.net', 'virginradio.fr', 'alisonangel.com', 'virginhigh.com', 'steamtraffic.com', 'virginscrazy.com', 'teachtwinks.com', 'thatsfucked.org', 'xtoplists.com', 'pornobanner.com', 'brazzers.com', 'sybianvirgins.com', 'onlybigmovies.com', 'angelday.info', 'playblog.ws', 'slothtraffic.com', 'dla3hotbanat.info', 'vibrasian.com', 'memebase.com', 'adsgangsta.com', 'stileproject.com', 'dutchangels.nl', 'homemadevids.net', 'sexualblondes.net', 'photonaturals.com', 'seekbang.com', 'cantender.com', 'evaevangelina.net', 'triplexangels.com', 'newsfilter.org', 'angelique.net', 'evaangelinax.com', 'virginpass.com', 'toteme.com', 'desadesangels.com', 'natursektcam.de', 'adultmoda.com', 'seo1.org', 'shabbyvirgins.com', 'milanohotels.org', '21x.org', 'meetlocals.com', 'rotanaz.com', 'angelsinsatin.com', 'angel4host.com', 'fpfreegals.com', '101sexsecret.com', 'oiledangels.com', 'persiankitty.com', 'topsiteuri.ro', 'fuckbook.cm', 'amourangels.com', 'photosex.biz', 'godefloration.net', 'virginhoney.com', 'tube8.com', '1stmovieclub.net', 'pornhd.xyz', 'freesexdoor.com', 'skypecam.com', 'xxx4live.com', 'ivanafukalot.com', 'nadiavirgin.com', 'cybertoplists.com', 'pornhub.com', 'sleazyangels.com', 'virginoff.com', '2damnhot.com', 'movie2k.to', 'buckangel.com', 'littlevirgin.com', 'karupsgals.com', 'animepornmov.com', 'sexytout.com', 'janesguide.com', 'sinisterangel.com', 'lifeselector.com', 'virginz.nl', 'xxxreactor.com', '7virgin.com', 'popcash.net', 'sexad.net', 'vipangelz.com', 'tendervirgins.com', 'pornoinside.com', 'ladylust.com', 'angelbaseball.com', 'sucksex.com', 'nastydisney.com', 'amateurseite.com', 'cupofsingles.com', 'angeldark.nl', 'virginladies.com', 'pussygreen.com', 'voffka.com', 'babedump.com', 'officesex101.com', 'cliter.com', 'virginshow.com', 'asiablue.com', 'sexyads.com', 'amateurgalls.com', 'rexmag.com', 'stepnation.com', 'cherrynovelty.com', 'tenderboys.net', 'changels.net', 'webtraffic.se', 'natursekt.bz', 'angelinalee.net', 'doubleviking.com', 'mpmcash.com', 'theangelina.com', 'phallosdei.com', 'nymphogirls.com', 'youngandhorny.com', 'xxxcounter.com', 'eurogalz.com', 'justmouthfuls.com', 'darkangel.com', 'moztna.com', 'desihotpoint.com', 'foaks.com', 'lookvirgin.com', 'wendise.com', 'muscleangels.com', 'elunesangels.com', 'upforit.com', 'eveangelina.net', 'virginidad.com', 'peachangel.com', 'sexdildoking.com', 'lisaangeline.com', 'orgasm.com', 'gabrio.com', 'virginsfresh.com', 'ez5ez5xxx.info', 'shyvirgins.com', '3animalsex.com', 'lezbohoneys.com', 'homosrus.com', 'realitykings.com', 'yanks.com', 'onlineangels.com', 'angellafaith.com', '007angels.com', 'onlyfatchiks.com', 'torontoangels.com', 'ass2waist.com', 'realsexdates.com', 'blackystars.com', 'pornclub.com', 'virginanime.com', 'magicmovies.com', 'sexlist.com', 'damnlinks.com', 'usvirgin.com', 'camelcookie.com', 'angelcassidy.com', 'allisonvirgin.com', 'asianxtv.com', 'cams.com', 'sharday.us', 'polandtoday.org', 'angelsamazing.com', 'angelicfilms.com', 'baisepartout.com', 'teensexmovs.com', 'maxesangels.com', 'virginidad.nl', 'yesmessenger.hu', 'angelatiger.com', 'onegaysex.com', 'war2kotshena.info', 'pornofolies.com', 'moonangel.com', 'atmovs.com', 'piporno.com', 'solotouch.com', 'facebooksexo.com', 'youjizz.com', 'amyvirgin.com', 'bangyoulater.com', 'mexicanvirgin.com', 'amateursexy.net', 'angelicabella.com', 'twistedblogs.com', 'bursasporteam.com', 'agangels.net', 'drstrangelove.com', 'tgirlmeat.com', 'refinery29.com', 'angel.se', 'gapingangels.com', 'bangbros1.com', 'angeldollars.com', 'angela.nl', 'neswangy.net', 'dreamangelsny.com', 'angelaryan.com', 'sicflics.com', 'angela.nu', 'eveangelpic.com', 'bwlesbians.com', 'arabictopics.com', 'perfectgirls.net', 'angelglam.com', 'hushaccess.com', 'bookmarklinks.com', 'hardissimo.org', 'fling.com', 'xkxempire.com', 'madthumbs.com', 'usvirgins.com', 'join4free.com', 'hentaitoonami.com', 'sancdn.net', 'mommygotboobs.com', 'sexygirlbutts.com', 'burningcamel.org', 'milfseeker.com', 'zasians.com', 'vidz.com', 'ayanaangel.com', 'bloodangels.com', 'angelika.de', 'streamlivesex.com', 'angelicmusick.com', 'angelplace.com', 'enature.net', 'pix4dicks.com', 'hardtobuy.com', '18yearsold.com', 'xtheatre.net', 'swissangels.ch', 'topsites24.net', 'video69.ru', 'angellong.com', 'felonyangel.com', 'freshpornline.com', 'clubrejal.com', 'livejasmin.net', 'panzertraffic.com', 'wifeysworld.ws', 'virgin4free.com', 'dvdboys.com', 'avalaurenblog.com', 'hardvirgins.com', 'holytaco.com', 'virginmobile.fr', 'angelataylor.org', 'angelcasting.net', 'webcamsdancer.com', 'exchangecash.de', 'myvirginity.com', '2001positions.com', 'kingpinmedia.net', '3x.ro', 'sksawi.info', 'sunporno.com', 'lilbabes.com', 'playingboy.com', 'extremebig.com', 'merryangels.com', 'zebkbeer.com', 'pervygames.com', 'sweetvirgin.com', 'reelgalleries.com', 'xgallsx.com', 'sex2inc.com', 'voyeurpornweb.com', 'eroticmatch.com', 'hardlicks.com', 'teensgotboobs.net', 'olgasangels.net', 'roccomovies.net', 'hardjpegs.com', 'strangeland.com', 'zmature.com', 'virgins.pl', 'hardasses.com', 'banatdream.com', 'hotpornshow.com', 'transladyboy.com', 'hitahottie.com', 'lemonmov.com', 'hookup.com', 'hotadultstuff.com', 'qualityporn.biz', 'onlybestsex.com', 'creamyangels.com', 'femjoyangels.com', 'traffic.ru', 'holylol.com', 'kittysangels.com', 'merryangels.info', 'rarbg.com', 'femdomdraw.com', 'latexangel.net', 'bitchdump.com', 'yumm.net', 'naturiste.be', 'virginalena.com', '9hz.com', 'britneyvirgin.com', 'yasalambanat.info', 'lezcuties.com', 'evavirgin.com', 'fetishdollars.net', 'gallfree.com', 'faithvirgin.com', 'iknowthatgirl.com', 'allteeens.com', 'scoreadate.com', 'chunkybutts.com', 'angelcam.nl', 'fatpichunter.com', 'sextvx.com', 'babelogbook.com', 'hardsu.net', 'pinkwebcam.com', 'gtaangels.net', 'a4w.cc', 'fuckbook.com', 'shareporno.com', 'porndisney.com', 'porn.to', 'ztod.com', 'davidsangels.net', 'charlisangels.com', 'angelband.org', 'hotarabchat.com', 'bannedcelebs.com', 'hardgirls.nl', 'angelsofmercy.org', 'hardlads.com', 'phonevirgin.com', 'jasminsangels.com', 'gogoangels.com', 'chaturbate.com', 'cartoonvalley.com', 'mangoangel.com', 'videos666.com', 'trailerwmv.com', 'glossyangels.info', 'besthotdates.com', 'rawtube.com', 'angelslinks.com', 'tootrash.com', 'daredorm.com', 'loa6.com', 'ddorfprivat.de', 'inthecrack.com', 'amateurmpeg.net', 'mofosex.com', 'redangels.se', 'hardhut.com', 'wunbuck.com', 'evangelio.com', 'swapfinder.com', 'crakmedia.com', 'picxx.net', 'pinkvisualpad.com', 'thumblogger.com', 'virginia.in', 'dumbvirgins.com', 'angelicasin.net', 'angelicasin.com', '2gfx.com', 'myhomeclip.com', 'jartna.com', 'virginmaleass.com', '1sexsex.com', 'sweethotteens.com', 'astridsangels.com', 'hqvirgins.com', 'superporbbaa.ru', 'nudegalleries.org', 'sextracker.com', 'gangbangsquad.com', 'smartmovies.net', 'angelsdublin.com', 'paixaogay.com', 'enaturist.com', 'pantyhosetv.net', 'yobt.com', 'angelicaheart.com', 'virginals.com', 'wisevirgin.com', 'annangelishot.com', 'kolyomfilm.com', 'gamelink.com', 'davecummings.com', 'angelswife.com', 'fuckyoucash.com', 'adamandeve.com', 'virginfisters.net', 'virgingaming.com', 'virginstories.com', 'virginsmag.com', 'lingeriesins.com', 'siska.tv', 'videovirgins.com', 'blackangelica.com', 'pussisex.com', 'tatagirls.com', 'greatvirgins.com', 'escort23.com', 'pornopim.com', 'doublepimp.com', 'daclick.com', 'angelaathomas.com', 'topbucks.com', 'mmaaxx.com', 'adultdvdhits.com', 'naturists.com', 'keezmovies.com', 'kagbz.com', 'vidbang.com', 'amaland.com', 'angelinarossi.com', 'jizzads.com', 'usasexlovers.com', 'payserve.com', 'virginsclub.com', 'sassyangel.com', 'tastyangels.com', 'elitedollars.com', 'juggsarea.com', 'salamtakehoh.info', 'myanalangel.com', 'rk.com', 'arabvirgins.com', 'picahottie.com', 'pokeherstars.com', 'frhsex.com', 'myjizztube.com', 'angelfier.com', 'voktel.com', 'huntedangels.com', 'slumsluts.net', 'naturalangels.com', 'sxx.com', 'footangels.com', 'angelinacrow.org', 'az7t2.com', 'amazingsexx.com', 'qoqoz.com', 'hostave4.net', 'yesmessenger.eu', 'angelamelini.com', 'badvirgins.com', 'hobomovies.com', 'neangel.com', 'alivegirls.com', 'ibannerx.com', 'arab66.com', 'foxyreviews.com', 'mystarlets.com', 'moviemonster.com', 'privatecams.ws', 'angelclip.info', 'mozazbnat.info', 'danimiles.com', 'arabks.com', 'rumrunners.us', 'virgincity.com', 'virginsexweb.com', 'arbkos.com', 'angelina.cz', 'blacksnake.com', 'chickenhost.com', 'angel20.com', 'ixtractor.com', 'hqgal.com', 'lostangel.ws', 'trueangels.com', 'angelslinks.net', 'fleshlight.com', 'toptoonsites.com', 'angelochec.net', 'dicktricks.com', 'wicked.com', 'virgintime.com', 'xxxvogue.net', 'angelmpegs.com', 'richardkern.com', 'virginz.tv', 'angelbabedebs.com', 'pornoxxxclips.com', 'evilangelppv.com', 'pcangel.com', 'virginoff.biz', 'boobscategory.com', 'amateurmatch.com', 'sleepingbitch.com', 'angelface.hu', 'omwex.com', 'natursekt24.com', 'wtfpeople.com','xvideo.com']


drives = win32api.GetLogicalDriveStrings()
drives1 = drives.split('\000')[:-1]
c = drives1[0]
for i in range(len(drives1)):
    if os.path.exists(drives1[i]+'windows')== True:
        c1=drives1[i]+'windows'
        break
    else:
        c1=drives1[0]
path=c
path1=c+"\\freedom"
try:
    os.makedirs(path + '\\freedom')
except:
    pass

class AppServerSvc1(win32serviceutil.ServiceFramework):
    _svc_name_ = "esfahanoud1"
    _svc_display_name_ = "esfahan oud1"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):

        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        #handele archive matneefail etesal dakheli
        lines = []
        while 1:
            try:
                    f = open(path1 + '\list1.txt', 'r')
                    line = f.readlines()
                    for c in line:
                        g = c.split('=')
                        if g[0] == 'archives':
                            arshiv = g[1]
                        if g[0] == 'mamnu':
                            lin1 = g[1].split(',')
                            for t in range(len(lin1)-1):
                                lines.append(lin1[t])
                    f.close()
                    break
            except IOError as e:
                pass
        if arshiv[0] == '1':
            lines = lines+aline
        self.timeout = 0
        mmm = True
        namebro = ['firefox.exe', 'iexplore.exe', 'chrome.exe']
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\Clients\StartMenuInternet', 0,
                                 winreg.KEY_READ)
            for i in xrange(0, winreg.QueryInfoKey(key)[0]):
                namebro.append(str(winreg.EnumKey(key, i)).lower())
        except:
            pass
        self.main(lines,namebro)
    def main(self,lines,namebro):

        while 1:
            try:
                response = urllib.urlopen("http://www.google.com")
                import socket
                import psutil
                mmm = True
                m = socket.gethostbyname(socket.gethostname())
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
                s.bind((m, 0))
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
                while mmm == True:
                    data = s.recvfrom(10000)
                    for i in range(len(lines)):
                        mm = lines[i]
                        #hengame arshive moshahedeshode etesal delete
                        if mm in str(data):
                            l=0
                            for process in (process for process in psutil.process_iter()):
                                for oo in range(len(namebro)):
                                    if process.name() == namebro[oo]:
                                       process.kill()
                                       l=l+1
                            if l == 0:
                                try:
                                    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                         r'SOFTWARE\Wow6432Node\Clients\StartMenuInternet', 0,
                                                         winreg.KEY_READ)
                                    for i in xrange(0, winreg.QueryInfoKey(key)[0]):
                                        if str(winreg.EnumKey(key, i)).lower() in namebro:
                                            pass
                                        else:
                                            namebro.append(str(winreg.EnumKey(key, i)).lower())
                                except:
                                    pass


                    rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
                    if rc == win32event.WAIT_OBJECT_0:
                        servicemanager.LogInfoMsg("esfahanoud1 - STOPPED!")  # For Event Log
                        mmm = False
                        break

                if mmm == False:
                    break
            except:
                pass
if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(AppServerSvc1)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(AppServerSvc1)

