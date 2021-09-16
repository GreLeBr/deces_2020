import numpy as np
import pandas as pd

# Load the CSV needed

def get_data():    
    df= pd.read_csv("/raw_data/deces_2020.csv", sep=";", encoding="utf-8")
    communes=pd.read_csv("/raw_data/commune2021.csv")
    movement=pd.read_csv("/raw_data/mvtcommune2021.csv")
    pays=pd.read_csv("/raw_data/pays2021.csv")
    return df, communes, movement, pays

def attribute_countries(df,communes,movement,pays):
    # Creating a column with birthplaces as string and normalized to 5 of length
    df["lieunaiss_str"]=df["lieunaiss"].astype("str")
    df["lieunaiss_str"]=df["lieunaiss_str"].apply(lambda x: "0"+x if len(x)<5 else x)   

    # Giving France as country of birth if the communes exists in the csv
    communes_com=[x for x in communes["COM"]]
    df.loc[df["lieunaiss_str"].isin(communes_com), "paysnaiss"] = "FRANCE"
    movement_COM_AV=[x for x in movement["COM_AV"]]

    # Giving France as country of birth if the communes exists in the csv    
    df.loc[df["lieunaiss_str"].isin(movement_COM_AV), "paysnaiss"] = "FRANCE"
    for x in ["PALALDA", "LOMPNES", "HAUTEVILLE-LOMPNES"]:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE"
    # Attributing country of birth /location outside of France metropolis 
    POLYNESIE=["ILES DU VENT", "ILES SOUS LES VENTS", "ARCHIPEL DES MARQUISES", "ARCHIPEL TUAMOTU", "ARCHIPEL TUBUAI", "PAPEETE" ,"TAPUTAPUATEA" ,"MOOREA-MAIAO" ,"TUMARAA" , \
            "PUNAAUIA","TEVA I UTA", "TAIARAPU-EST", "TAHAA", "TAIARAPU-OUEST","ARUE","TUBUAI", "UTUROA", "RAPA","FATU-HIVA", "BORA-BORA", "PIRAE", "HIVA-OA", "GAMBIER" , \
            "NUKU-HIVA" ,"UA-POU","HUAHINE","MAUPITI","NAPUKA","RURUTU", "FAAA","RANGIROA","ANAA","HIKUERU", "PAEA", "RAIVAVAE","HAO", "PAPARA", "TATAKOTO","MAKEMO", "FAKARAVA", \
            "TAKAROA", "RIMATARA", "HITIAA O TE RA", "TAHUATA","MAHINA","PUKAPUKA", "REAO", "FANGATAU", "UA-HUKA","MANIHI", "FANGATAU","ARUTUA","NUKUTAVAKE", "TUREIA"]
    for x in POLYNESIE:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(POLYNESIE)"

    POLYNESIE_code=[str(x) for x in range(98711, 98759)]
    for x in POLYNESIE_code:
        mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(POLYNESIE)"

    CALEDONIE=["NOUVELLE CALEDONIE","TOUHO","THIO", "POYA", "POINDIMIE", "OUVEA", "NOUMEA","LE MONT-DORE", "KOUMAC","CANALA", "MARE","LIFOU", "HIENGHENE","PAITA", "DUMBEA", \
            "HOUAILOU"]
    for x in CALEDONIE:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(NOUVELLE_CALEDONIE)"

    CALEDONIE_code=[str(x) for x in range(98801, 98834)]
    for x in CALEDONIE_code:
        mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(NOUVELLE_CALEDONIE)"

    MAYOTTE=["M'TSANGAMOUJI", "COLL TERR MAYOTTE", "KANI-KELI", "BANDRELE", "TSINGONI", "MAMOUDZOU", "SADA", "BOUENI" ,"CHIRONGUI", "CHICONI", "BANDRABOUA" ,"DZAOUDZI", \
            "PAMANDZI","ACOUA","MTSAMBORO","KOUNGOU", "OUANGANI","DEMBENI"]
    for x in MAYOTTE:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(MAYOTTE)"  

    MAYOTTE_code=[str(x) for x in range(97601, 97618)]
    for x in MAYOTTE_code:
        mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(MAYOTTE)"

    WALIS=["ARCHIPEL WALLIS ET FUTUNA" , "ALO", "UVEA", "SIGAVE"]
    for x in WALIS:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(WALIS_FUTUNA)"  

    REUNION=["REUNION"]
    for x in REUNION:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(REUNION)"  

    SAINT_PIERRE=["SAINT-PIERRE", "MIQUELON-LANGLADE"]
    for x in SAINT_PIERRE:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(SAINT-PIERRE)"  

    SAINT_MARTIN=["SAINT-MARTIN"]
    for x in SAINT_MARTIN:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(SAINT-MARTIN)"

    SAINT_BARTHELEMY =["97701"]
    for x in SAINT_BARTHELEMY:
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(SAINT-BARTHELEMY)"

    Terres_australes=[str(x) for x in range(98411, 98416)]
    for x in Terres_australes:
        mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(TERRES_AUSTRALES)"

    ILE_DE_CLIPPERTON=["98901"]
    for x in ILE_DE_CLIPPERTON:
        mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="FRANCE(ILE_DE_CLIPPERTON)"
    # Attributing a country of birth for places which have several entries in pays2021.csv
    ENGLAND=["99132"]
    for x in ENGLAND:
        mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"{x}") 
        df.loc[mask,"paysnaiss" ]="ENGLAND"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99101") 
    df.loc[mask,"paysnaiss" ]="DANEMARK"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99103") 
    df.loc[mask,"paysnaiss" ]="NORWAY"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99135") 
    df.loc[mask,"paysnaiss" ]="NETHERLANDS"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99223") 
    df.loc[mask,"paysnaiss" ]="INDIA"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99308") 
    df.loc[mask,"paysnaiss" ]="ZANZIBAR"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99313") 
    df.loc[mask,"paysnaiss" ]="SPAIN"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99404") 
    df.loc[mask,"paysnaiss" ]="USA"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99425") 
    df.loc[mask,"paysnaiss" ]="ISLANDS"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99427") 
    df.loc[mask,"paysnaiss" ]="ENGLAND"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99432") 
    df.loc[mask,"paysnaiss" ]="USA"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99501") 
    df.loc[mask,"paysnaiss" ]="AUSTRALIA"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99502") 
    df.loc[mask,"paysnaiss" ]="NEW-ZEALAND"

    mask=(df["paysnaiss"].isnull()==True)  & (df["lieunaiss_str"]==f"99505") 
    df.loc[mask,"paysnaiss" ]="USA"

    # Adding France to entries with French birthplace but no written location
    for x in range (100):
        mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]==f"DEPARTEMENT {x:02d}") 
        df.loc[mask,"paysnaiss" ]="FRANCE"

    # Adding France / previous colony for past French colonies
    Algerie_francaise=["DEPARTEMENT D'ORAN", "DEPARTEMENT D'ALGER", "DEPARTEMENT DE CONSTANTINE", "SUD DE L'ALGERIE"]
    for dep in Algerie_francaise:
        mask=((df["paysnaiss"].isnull()==True) & (df["commnaiss"]==dep))
        df.loc[mask, "paysnaiss"]="FRANCE(ALGERIE)"

    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIENNE GUINEE") 
    df.loc[mask,"paysnaiss" ]="FRANCE(GUINEE)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIENNE COTE D'IVOIRE") 
    df.loc[mask,"paysnaiss" ]="FRANCE(COTE D'IVOIRE)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="SOUDAN FRANCAIS") 
    df.loc[mask,"paysnaiss" ]="FRANCE(SOUDAN)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="EX-DAHOMEY") 
    df.loc[mask,"paysnaiss" ]="FRANCE(BENIN)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="TERR FRANCAIS AFARS ISSAS") 
    df.loc[mask,"paysnaiss" ]="FRANCE(DJIBOUTI)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="MOYEN CONGO") 
    df.loc[mask,"paysnaiss" ]="FRANCE(CONGO)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN GABON") 
    df.loc[mask,"paysnaiss" ]="FRANCE(GABON)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN MADAGASCAR") 
    df.loc[mask,"paysnaiss" ]="FRANCE(MADAGASCAR)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN SENEGAL") 
    df.loc[mask,"paysnaiss" ]="FRANCE(SENEGAL)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN CAMEROUN") 
    df.loc[mask,"paysnaiss" ]="FRANCE(CAMEROUN)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="OUBANGUI CHARI") 
    df.loc[mask,"paysnaiss" ]="FRANCE(CENTRAFRIQUE)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN TOGO") 
    df.loc[mask,"paysnaiss" ]="FRANCE(TOGO)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN TCHAD") 
    df.loc[mask,"paysnaiss" ]="FRANCE(TCHAD)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN MAURITANIE") 
    df.loc[mask,"paysnaiss" ]="FRANCE(MAURITANIE)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN NIGER") 
    df.loc[mask,"paysnaiss" ]="FRANCE(NIGER)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANC CODOM FRANC-BRIT") 
    df.loc[mask,"paysnaiss" ]="FRANCE(VANUATU)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="ANCIEN NIGER") 
    df.loc[mask,"paysnaiss" ]="FRANCE(NIGER)"
    mask=(df["paysnaiss"].isnull()==True)  & (df["commnaiss"]=="EX-HAUTE VOLTA") 
    df.loc[mask,"paysnaiss" ]="FRANCE(BURKINA FASO)"

    # Adding missing countries for birthplace 
    mask=df["paysnaiss"].isnull()==True
    for s in df.loc[mask,"lieunaiss_str"]:
        if s in [x for x in pays["COG"] if pays[pays["COG"]==x].shape[0]<2]:
            mask_1=(df["paysnaiss"].isnull()==True) & (df["lieunaiss_str"]==s) 
            mask_2=pays["COG"]==s
            df.loc[mask_1, "paysnaiss"]=pays.loc[mask_2, "LIBCOG"].values[0]

    # Updating birthplace with current zip code

    dict_value={k:v for k,v in zip(movement["COM_AV"], movement["COM_AP"])}
    df["lieunaiss_str"]=df["lieunaiss_str"].apply(lambda x: dict_value[x] if x in dict_value.keys() else x)

    return df