# Portfolio — cau truc thu muc

```
index.html                  trang chinh (hero, focus, CV, publications, footer)
cards/                      moi nghien cuu mot file, sua rieng tung file
  01-fast-eis.html          Fast EIS bang PRBS + wavelet
  02-aln.html               Gom AlN, dai nhiet do rong
  03-nvp-lvp.html           NVP / LVP, dan ion-dien tu hon hop
  04-electrolytes.html      Dien giai polymer va long, Nernst-Planck
  05-llzo.html              LLZO, vuot qua brick-layer
  06-bioimpedance.html      Tro khang co the nguoi
sections/                   hai danh sach dai, sua rieng tung file
  projects.html             danh sach du an (dat truoc Research activity)
  presentations.html        danh sach bao cao hoi nghi (dat sau Publications)
figures/                    toan bo anh (bao gom ca portrait.jpg)
build.py                    (tuy chon) gop tat ca thanh mot file duy nhat
```

## Sua noi dung

- Sua mot nghien cuu: mo dung file trong `cards/`, khong dong vao `index.html`.
- Them nghien cuu moi: chep mot file trong `cards/` ra ten moi, sua noi dung,
  roi them mot dong vao `index.html` trong khoi "CAC CARD NGHIEN CUU":

  ```html
  <div class="card-slot" data-src="cards/07-ten-moi.html"></div>
  ```

- Doi thu tu cac card: doi thu tu cac dong `card-slot` trong `index.html`.
- Sua danh sach du an: `sections/projects.html`.
- Sua danh sach bao cao hoi nghi: `sections/presentations.html`.
  Trong hai file nay, cho nao con chu `TODO` la cho con thieu du lieu.
- Sua phan gioi thieu, CV, danh sach cong bo: van o trong `index.html`.
- Anh moi: bo vao `figures/`, trong card ghi `src="figures/ten-anh.png"`.

## Xem trang

Cac card duoc nap bang `fetch()`, nen KHONG hien khi mo truc tiep bang
`file://` (nhay doi chuot). Chon mot trong hai cach:

1. Chay web server tinh trong thu muc nay:

   ```
   python -m http.server 8000
   ```

   roi mo http://localhost:8000

2. Hoac gop thanh mot file duy nhat de mo truc tiep / gui cho nguoi khac:

   ```
   python build.py
   ```

   -> tao `index_standalone.html`, mo bang trinh duyet la duoc.

Khi dat len GitHub Pages / Netlify / server cua truong thi khong can lam gi
them: `index.html` tu nap `cards/`.

## Con thieu

`figures/portrait.jpg` — chep anh chan dung vao thu muc `figures/`
(hoac sua lai duong dan trong `index.html` neu de o cho khac).
