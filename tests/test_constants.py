from scopus_of_science import constants as con

class Test_constants():
    def test_S_TAGS(self):
        S_TAGS = ['Authors', 'Author(s) ID', 'Title', 'Year', 'Source title', 'Volume', 'Issue', 'Art. No.', \
                'Page start', 'Page end', 'Page count', 'Cited by', 'DOI', 'Link', 'Affiliations', 'Authors with affiliations', \
                'Abstract', 'Chemicals/CAS', 'Tradenames', 'Manufacturers', 'Funding Details', 'Funding Text 1', 'Funding Text 2', \
                'References', 'Correspondence Address', 'Editors', 'Sponsors', 'Publisher', 'Conference name', 'Conference date', \
                'Conference location', 'Conference code', 'ISSN', 'ISBN', 'CODEN', 'PubMed ID', 'Language of Original Document', \
                'Abbreviated Source Title', 'Document Type', 'Publication Stage', 'Access Type', 'Source', 'EID']

        assert con.S_TAGS == S_TAGS
    
    def test_DIC(self):
        DIC = {
                'AU' : 'Authors',
                'TI' : 'Title',
                'PY' : 'Year',
                'SO' : 'Source title',
                'VL' : 'Volume',
                'IS' : 'Issue',
                'AR' : 'Art. No.',
                'BP' : 'Page start',
                'EP' : 'Page end',
                'PG' : 'Page count',
                'DI' : 'DOI',
                'AB' : 'Abstract',
                'BE' : 'Editors',
                'PU' : 'Publisher',
                'CT' : 'Conference name',
                'CY' : 'Conference date',
                'CL' : 'Conference location',
                'SN' : 'ISSN',
                'BN' : 'ISBN',
                'PM' : 'PubMed ID',
                'LA' : 'Language of Original Document',
                'J9' : 'Abbreviated Source Title',
                'DT' : 'Document Type',
                'OA' : 'Access Type', 
                'FU' : 'Funding Details',
                }

        assert con.DIC == DIC

