--  aggregate jumlah data harian pada masing-masing tabel

-- tabel dataMicrosite.csv
-- Untuk Mendapatkan Date swab
    SELECT swabDate, COUNT(swabDate) AS CountDateOfSwab 
    FROM db_microsite.`user` 
    GROUP BY swabDate
    ORDER BY swabDate ASC;

-- Untuk Mendapatkan Date antigen
    SELECT antigenDate, COUNT(antigenDate) AS CountDateOfAntigen 
    FROM db_microsite.`user` 
    GROUP BY antigenDate
    ORDER BY antigenDate ASC;

-----------------------------------------------------------------------------------------

-- tabel DataEhac.csv
