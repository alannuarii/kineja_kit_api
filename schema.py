from pydantic import BaseModel

class Unit(BaseModel):
    id = int
    nama_unit = str

    class Config:
        orm_mode = True


class Spesifikasi(BaseModel):
    id = int
    unit = str
    nama_mesin = str
    tipe_mesin = str
    serial_number = str
    tahun_operasi = str
    dtp = str
    dmn = str
    unit_id = int

    class Config:
        orm_mode = True


class Pengusahaan(BaseModel):
    id = int
    periode = str
    produksi = float
    ps_sentral = float
    ps_trafo = float
    bbm = float
    batubara = float
    po = float
    mo = float
    fo = float
    fo_omc = float
    sh = float
    rsh = float
    ph = float
    epdh = float
    eudh = float
    esdh = float
    efdhrs = float
    trip_internal = int
    trip_eksternal = int
    spesifikasi_id = int

    class Config:
        orm_mode = True