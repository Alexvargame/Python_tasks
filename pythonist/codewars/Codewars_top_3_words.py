import re
def top_3_words(text):
    res=[]
    text_dict={}
    print(text)
    text=re.sub('["/","\n","?","_","\n",":","!",".",",","-",";","-"]', ' ', text)
    print(text)
    txt_spl=re.split(r'[\-\_\s+]',text)
    print(txt_spl)
    text_lst=[wl.lower().strip('_-') for wl in txt_spl]
    for word in text_lst:
        key,value=text_lst.count(''.join([w for w in word.lower() if w.isalpha() or w=="'"])),''.join([w for w in word.lower() if w.isalpha() or w=="'"])
        l=text_dict.get(key,[])
        if value not in l and value!='' and set([v for v in list(value)])!={"'"}:
            l.append(value)
        text_dict[key]=l
    print(text_lst)
    print(text_dict)
    for key  in dict(sorted(text_dict.items(),reverse=True)).keys():
        res.extend(text_dict[key])
        if len(res)>3:
            return res[:3]
    return res




        
def main():

##    print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
##                         mind, there lived not long since one of those gentlemen that keep a lance
##                        in the lance-rack, an old buckler, a lean hack, and a greyhound for
##                        coursing. An olla of rather more beef than mutton, a salad on most
##                        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
##                        on Sundays, made away with three-quarters of his income."""))
     print(top_3_words("""mHFqiI_!pNzigM :?;-iqdo?.?/!CKdqB_?G'CsxlU!_?EfzSn,G'CsxlU!CKdqB? ;_lMBOe?-?__pNzigM .,?G'CsxlU:lMBOe , -!EfzSn, :?G'CsxlU?pNzigM!/;.pNzigM!.G'CsxlU:: !EfzSn! ?CKdqB_/;//lMBOe/_?;!mHFqiI:? ?,iqdo;::_lMBOe.;mHFqiI,_CKdqB,.;!_iqdo!:,/;pNzigM-_.iqdo:::,?pNzigM:iqdo? /.pNzigM/.-mHFqiI!?,-CKdqB-/lMBOe._mHFqiI.lMBOe.,.  CKdqB?_? .mHFqiI -;!_CKdqB.;iqdo-? _-G'CsxlU?!///iqdo_,:_ CKdqB;; CKdqB- ?!mHFqiI!,;!?lMBOe_pNzigM-:G'CsxlU_,._mHFqiI:?mHFqiI:-._:pNzigM- ;;!EfzSn:CKdqB;_ .!pNzigM;.?;/mHFqiI_-mHFqiI, :!;lMBOe/_,_pNzigM,;pNzigM./..:lMBOe-:CKdqB.?.G'CsxlU-::,_iqdo: _mHFqiI? /._EfzSn,CKdqB/:/!;EfzSn.CKdqB ,mHFqiI,:.?.EfzSn---pNzigM./mHFqiI;G'CsxlU_._ -CKdqB, .EfzSn_- ;mHFqiI!;?G'CsxlU_? /mHFqiI_EfzSn/?!:iqdo?,,-.iqdo,, ;mHFqiI:,?!!mHFqiI!:?,mHFqiI;_pNzigM_,-lMBOe/pNzigM;lMBOe/!.pNzigM,.-mHFqiI? iqdo_pNzigM:!;/CKdqB pNzigM.EfzSn:G'CsxlU/:!.iqdo! ?-.pNzigM_/pNzigM/lMBOe,!,,:lMBOe!/-?/pNzigM?/-CKdqB./-;G'CsxlU.pNzigM-_lMBOe._iqdo lMBOe G'CsxlU?./;-G'CsxlU,/iqdo_pNzigM.?,-lMBOe?lMBOe-G'CsxlU:/"""))
     print(top_3_words("""BLdzQ_?;.?FoP_HdgjoqAIBT!:?;PWqh_?PXy/.:!vWb :-!iJSKSZaybM,jVmU-? _SzF . FoP- ?culm-__DJXq'qUWFi_;??ZiEt;_.FoP.;!.iJSKSZaybM._;::PWqh.:FoP!?;culm!;-,HdgjoqAIBT!DJXq'qUWFi //.ZiEt?!:HdgjoqAIBT__BLdzQ .?!PXy:kYfrQe /!!?BLdzQ-?-iJSKSZaybM/._: PWqh_jVmU_,?ZiEt,.:/:OPYyfOrpE ;?.;FoP_SzF;?:..PWqh;iJSKSZaybM!;/d'';jVmU,/!/OPYyfOrpE-?/ ,iJSKSZaybM!::SzF;?.;PWqh.--/:d''/ PWqh?.,d'' : ?PWqh/_culm,,/?PWqh/ ;. culm_-DJXq'qUWFi -::BLdzQ;?/;PWqh!::!OPYyfOrpE:??/DJXq'qUWFi-BLdzQ?/,-SzF/    culm?:OPYyfOrpE!_-.,ZiEt-BLdzQ .PXy:?iJSKSZaybM/ ?;SzF..,/,culm,!_-,SzF-ZiEt._KeEa/,, culm:,_:!FoP_azxJYfhuX ;azxJYfhuX_:KeEa/_/?HdgjoqAIBT/:_!-PWqh-,-:SzF;PWqh/._DJXq'qUWFi-DJXq'qUWFi-!;;SzF:. / PXy ?!GkJWPYu  -GkJWPYu,PXy.!;.azxJYfhuX,PWqh.PXy;BLdzQ-/!azxJYfhuX_; VDKiFbrQIg,_!PXy__ OPYyfOrpE:--PXy  .iJSKSZaybM.culm,?.-?jVmU?-culm:d''!!PWqh;/;:SzF!jVmU.?_iJSKSZaybM ZiEt.!; /azxJYfhuX: __azxJYfhuX,-PWqh?iJSKSZaybM;,SzF; -.-culm: -.OPYyfOrpE,PWqh:;OPYyfOrpE ,_;:vWb/PXy_? :ZiEt!,,!PWqh;PXy.? culm  - ;FoP?_ BLdzQ:!_PXy---BLdzQ/FoP_ jVmU/ :_!SzF_,.SzF!?FoP,!KeEa!;:KeEa;_. PXy,_!DJXq'qUWFi!culm:_; GkJWPYu,!ZiEt/.-SzF.!_ BLdzQ azxJYfhuX,?.:PWqh:/PXy;.vWb azxJYfhuX, ,; DJXq'qUWFi!OPYyfOrpE!?,PWqh/:PWqh_ vWb__.iJSKSZaybM? ._.DJXq'qUWFi?;!-VDKiFbrQIg;-culm/_ ?culm/,!,_PWqh;?:ZiEt:!? jVmU BLdzQ/.!:culm:;culm .-FoP???BLdzQ_OPYyfOrpE-DJXq'qUWFi/-HdgjoqAIBT/PXy/SzF..!FoP:,, .PWqh:/PXy;:_OPYyfOrpE ,:!ZiEt;!OPYyfOrpE.iJSKSZaybM_ -:.HdgjoqAIBT.ZiEt?PXy; ,  PXy_,FoP?_PXy: PXy.,!?!SzF OPYyfOrpE?!:/,culm:.-//FoP_?iJSKSZaybM/_;BLdzQ.:.:PXy_?FoP-OPYyfOrpE.GkJWPYu . ??PWqh,FoP,.iJSKSZaybM!BLdzQ;!BLdzQ??:.azxJYfhuX/!._OPYyfOrpE.,;SzF!-;:azxJYfhuX_   GkJWPYu?.HdgjoqAIBT?;_;/OPYyfOrpE :_/-PWqh:./SzF?:,HdgjoqAIBT,,iJSKSZaybM:.;!culm:? _DJXq'qUWFi/,-;,d''.?-DJXq'qUWFi?.:/ZiEt??SzF;/!;,iJSKSZaybM!;_?:BLdzQ,_;.OPYyfOrpE:,,./PWqh-!-?-azxJYfhuX:!?-?culm_,;ZiEt!. .:DJXq'qUWFi;_?,SzF-;_ PXy,DJXq'qUWFi;FoP, _culm/;;;,BLdzQ_ DJXq'qUWFi  ?FoP,- d'',SzF ,!.DJXq'qUWFi.:ZiEt?/ _BLdzQ;:;-PWqh,!SzF KeEa,_;,/ZiEt.azxJYfhuX.!?SzF:.d''/..!KeEa-DJXq'qUWFi/:: /PWqh?iJSKSZaybM! SzF!  ?azxJYfhuX,?;PWqh;.!?FoP//_:SzF-FoP,DJXq'qUWFi?DJXq'qUWFi/-/_:FoP_, OPYyfOrpE,?PWqh,,vWb_,?culm-!! _SzF?jVmU-DJXq'qUWFi;;?,iJSKSZaybM/culm!/_ FoP  ?PXy/-/;-OPYyfOrpE!PWqh-,,.d''.:._;BLdzQ-_DJXq'qUWFi.!!:_BLdzQ:,PXy/culm_-_HdgjoqAIBT;;:,DJXq'qUWFi_/culm ,culm-,!/SzF;!?FoP/- culm-:??,vWb/GkJWPYu?BLdzQ?;___ZiEt!BLdzQ,-/PXy ,ZiEt;: .KeEa,/FoP, ?iJSKSZaybM.?!.culm.:-PWqh!?_;!PXy;/_!FoP/!/PXy!:vWb._ ;OPYyfOrpE.FoP ;_ DJXq'qUWFi:;d'' ,/PXy:-culm /GkJWPYu.PXy:/:;_PXy_FoP/_ ;,OPYyfOrpE?.!;?DJXq'qUWFi; ?-KeEa_; :DJXq'qUWFi ;._.DJXq'qUWFi-?;?!iJSKSZaybM?;;-!ZiEt:PXy_;SzF;-.! SzF/DJXq'qUWFi.. !SzF!FoP?;ZiEt///"""))
if __name__ == "__main__":
    main()




#
