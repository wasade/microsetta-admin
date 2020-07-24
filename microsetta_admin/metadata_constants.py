MISSING_VALUE = 'not provided'

# standard fields that are set based on sampling site
ENV_LOOKUP = {
    'Animal Habitat':
    {'sample_group': 'animal habitat',
     'scientific_name': 'metagenome',
     'taxon_id': '256318',
     'env_material': 'animal-associated habitat',
     'empo_1': 'Host-associated',
     'empo_2': 'Animal',
     'empo_3': 'Animal corpus',
     'env_package': 'host-associated',
     'ENV_FEATURE': 'animal-associated habitat',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project animal habitat sample',
     'sample_type': 'animal-associated',
     },
    'Biofilm':
    {'sample_group': 'biofilm',
     'scientific_name': 'biofilm metagenome',
     'taxon_id': '718308',
     'env_material': 'organic material',
     'env_package': 'microbial mat/biofilm',
     'empo_1': 'Host-associated',
     'empo_2': 'Animal',
     'empo_3': 'Animal corpus',
     'ENV_FEATURE': 'biofilm',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project biofilm sample',
     'sample_type': 'biofilm'
     },
    'Dust':
    {'sample_group': 'indoor',
     'scientific_name': 'Dust metagenome',
     'taxon_id': '1236744',
     'env_material': 'dust',
     'env_package': 'built-environment',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Surface (non-saline)',
     'ENV_FEATURE': 'environmental material',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project dust sample',
     'sample_type': 'dust'
     },
    'Food':
    {'sample_group': 'food',
     'scientific_name': 'food metagenome',
     'taxon_id': '870726',
     'env_material': 'food product',
     'env_package': 'misc environment',
     'ENV_FEATURE': 'anthropogenic environmental material',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Surface (non-saline)',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project food sample',
     'sample_type': 'food'
     },
    'Fermented Food':
    {'sample_group': 'food',
     'scientific_name': 'Food fermentation metagenome',
     'taxon_id': '1154581',
     'env_material': 'fermented food product',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Surface (non-saline)',
     'env_package': 'misc environment',
     'ENV_FEATURE': 'anthropogenic environmental material',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project fermented food sample',
     'sample_type': 'food'
     },
    'Indoor Surface':
    {'sample_group': 'indoor',
     'scientific_name': 'Indoor metagenome',
     'taxon_id': '1256227',
     'env_material': 'dust',
     'env_package': 'built environment',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Surface (non-saline)',
     'ENV_FEATURE': 'building',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project indoor surface sample',
     'sample_type': 'dust'
     },
    'Outdoor Surface':
    {'sample_group': 'outdoor',
     'scientific_name': 'ecological metagenome',
     'taxon_id': '410657',
     'env_material': 'surface layer',
     'env_package': 'misc environment',
     'ENV_FEATURE': 'building',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Surface (non-saline)',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project outdoor surface sample',
     'sample_type': 'surface'
     },
    'Plant habitat':
    {'sample_group': 'outdoor',
     'scientific_name': 'plant metagenome',
     'taxon_id': '1297885',
     'env_material': 'organic material',
     'env_package': 'plant-associated',
     'ENV_FEATURE': 'environmental material',
     'empo_1': 'Host-associated',
     'empo_2': 'Plant',
     'empo_3': 'Plant surface',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project plant habitat sample',
     'sample_type': 'plant'
     },
    'Soil':
    {'sample_group': 'outdoor',
     'scientific_name': 'soil metagenome',
     'taxon_id': '410658',
     'env_material': 'soil',
     'env_package': 'soil',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Soil (non-saline)',
     'ENV_FEATURE': 'soil',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project soil sample',
     'sample_type': 'soil'
     },
    'Sole of shoe':
    {'sample_group': 'indoor',
     'scientific_name': 'Dust metagenome',
     'taxon_id': '1236744',
     'env_material': 'dust',
     'env_package': 'built-environment',
     'empo_1': 'Host-associated',
     'empo_2': 'Animal',
     'empo_3': 'anthropogenic sample',
     'ENV_FEATURE': 'anthropogenic environmental material',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project dust sample',
     'sample_type': 'dust'
     },
    'Water':
    {'sample_group': 'water',
     'scientific_name': 'freshwater metagenome',
     'taxon_id': '449393',
     'env_material': 'water',
     'env_package': 'water',
     'empo_1': 'Free-living',
     'empo_2': 'Non-saline',
     'empo_3': 'Water (non-saline)',
     'ENV_FEATURE': 'environmental material',
     'ENV_BIOME': 'dense settlement biome',
     'description': 'American Gut Project water sample',
     'sample_type': 'water'
     }
}


HUMAN_SITE_INVARIANTS = {
    'Blood (skin prick)':
        {'body_product': 'UBERON:sebum',
         'sample_type': 'Blood (skin prick)',
         'scientific_name': 'human blood',
         'taxon_id': 'NA',
         'empo_3': 'Animal corpus',
         'body_habitat': 'UBERON:blood',
         'env_material': 'blood',
         'env_package': 'human-associated',
         'description': 'American Gut Project blood skin prick sample',
         'body_site': 'UBERON:blood'},
    'Hair':
        {'body_product': 'UBERON:sebum',
         'sample_type': 'Hair',
         'scientific_name': 'human skin metagenome',
         'taxon_id': '539655',
         'body_habitat': 'UBERON:hair',
         'empo_3': 'Animal surface',
         'env_material': 'sebum',
         'env_package': 'human-associated',
         'description': 'American Gut Project Hair sample',
         'body_site': 'UBERON:hair'},
    'Nares': {
        'body_product': 'UBERON:mucus',
        'sample_type': 'Nares',
        'scientific_name': 'human nasal/pharyngeal metagenome',
        'taxon_id': '1131769',
        'body_habitat': 'UBERON:nose',
        'env_material': 'mucus',
        'empo_3': 'Animal surface',
        'env_package': 'human-skin',
        'description': 'American Gut Project Nares sample',
        'body_site': 'UBERON:nostril'},
    'Vaginal mucus': {
        'body_product': 'UBERON:mucus',
        'sample_type': 'Vaginal mucus',
        'scientific_name': 'human vaginal metagenome',
        'taxon_id': '1632839',
        'body_habitat': 'UBERON:vagina',
        'empo_3': 'Animal secretion',
        'env_material': 'mucus',
        'env_package': 'human-vaginal',
        'description': 'American Gut Project Vaginal mucus sample',
        'body_site': 'UBERON:vaginal introitus'},
    'Sole of foot': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Sole of foot',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'env_material': 'sebum',
        'env_package': 'human-skin',
        'empo_3': 'Animal surface',
        'description': 'American Gut Project Sole of foot sample',
        'body_site': 'UBERON:skin of foot'},
    'Nasal mucus': {
        'body_product': 'UBERON:mucus',
        'sample_type': 'Mucus',
        'scientific_name': 'human nasal/pharyngeal metagenome',
        'taxon_id': '1131769',
        'body_habitat': 'UBERON:nose',
        'env_material': 'mucus',
        'empo_3': 'Animal secretion',
        'env_package': 'human-associated',
        'description': 'American Gut Project Nasal mucus sample',
        'body_site': 'UBERON:nostril'},
    'Stool': {
        'body_product': 'UBERON:feces',
        'sample_type': 'Stool',
        'scientific_name': 'human gut metagenome',
        'taxon_id': '408170',
        'empo_3': 'Animal distal gut',
        'body_habitat': 'UBERON:feces',
        'env_material': 'feces',
        'env_package': 'human-gut',
        'description': 'American Gut Project Stool sample',
        'body_site': 'UBERON:feces'},
    'Forehead': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Forehead',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'empo_3': 'Animal surface',
        'env_material': 'sebum',
        'env_package': 'human-skin',
        'description': 'American Gut Project Forehead sample',
        'body_site': 'UBERON:skin of head'},
    'Tears': {
        'body_product': 'UBERON:tears',
        'sample_type': 'Tears',
        'scientific_name': 'human eye metagenome',
        'taxon_id': '1774142',
        'body_habitat': 'UBERON:eye',
        'empo_3': 'Animal surface',
        'env_material': 'tears',
        'env_package': 'human-associated',
        'description': 'American Gut Project Tears sample',
        'body_site': 'UBERON:eye'},
    'Right hand': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Right Hand',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'empo_3': 'Animal surface',
        'env_material': 'sebum',
        'env_package': 'human-skin',
        'description': 'American Gut Project Right Hand sample',
        'body_site': 'UBERON:skin of hand'},
    'Axilla': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Axilla',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'env_material': 'sebum',
        'empo_3': 'Animal surface',
        'env_package': 'human-skin',
        'description': 'American Gut Project Right Axilla sample',
        'body_site': 'UBERON:skin of axilla'},
    'Torso': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Torso',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'empo_3': 'Animal surface',
        'ENV_MATTER': 'sebum',
        'description': 'American Gut Project torso sample',
        'body_site': 'UBERON:skin of trunk'},
    'Left leg': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Left leg',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'ENV_MATTER': 'sebum',
        'empo_3': 'Animal surface',
        'description': 'American Gut Project left leg sample',
        'body_site': 'UBERON:skin of leg'},
    'Right leg': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Right leg',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'ENV_MATTER': 'sebum',
        'empo_3': 'Animal surface',
        'description': 'American Gut Project right leg sample',
        'body_site': 'UBERON:skin of leg'},
    'Mouth': {
        'body_product': 'UBERON:saliva',
        'sample_type': 'Mouth',
        'scientific_name': 'human oral metagenome',
        'taxon_id': '447426',
        'body_habitat': 'UBERON:oral cavity',
        'env_material': 'saliva',
        'env_package': 'human-oral',
        'empo_3': 'Animal secretion',
        'description': 'American Gut Project Mouth sample',
        'body_site': 'UBERON:tongue'},
    'Left hand': {
        'body_product': 'UBERON:sebum',
        'sample_type': 'Left Hand',
        'scientific_name': 'human skin metagenome',
        'taxon_id': '539655',
        'body_habitat': 'UBERON:skin',
        'env_material': 'sebum',
        'env_package': 'human-skin',
        'empo_3': 'Animal surface',
        'description': 'American Gut Project Left Hand sample',
        'body_site': 'UBERON:skin of hand'},
    'Ear wax': {
        'body_product': 'UBERON:cerumen',
        'sample_type': 'Ear wax',
        'scientific_name': 'human metagenome',
        'taxon_id': '646099',
        'body_habitat': 'UBERON:ear',
        'env_material': 'ear wax',
        'env_package': 'human-associated',
        'description': 'American Gut Project Ear wax sample',
        'empo_3': 'Animal secretion',
        'body_site': 'UBERON:external auditory meatus'}
}


for site in HUMAN_SITE_INVARIANTS.values():
    site.update({
        'host_taxid': '9606',
        'scientific_name': 'human gut metagenome',
        'title': 'American Gut Project',
        'assigned_from_geo': 'Yes',
        'env_biome': 'dense settlement biome',
        'env_feature': 'human-associated habitat',
        'dna_extracted': 'Yes',
        'empo_1': 'Host-associated',
        'empo_2': 'Animal',
        'physical_specimen_remaining': 'Yes',
        'physical_specimen_location': 'UCSDMI',
        'host_common_name': 'human'})
