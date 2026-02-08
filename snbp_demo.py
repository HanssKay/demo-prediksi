# app_prediksi_ptn_tabs_fixed.py
import streamlit as st

st.set_page_config(page_title="Sistem Prediksi PTN", layout="centered")

# ========== TITLE ==========
st.title("🎓 SISTEM PREDIKSI SELEKSI MASUK PTN")
st.markdown("**SNBP & SNBT dalam satu sistem** - Prototipe untuk Skripsi")
st.divider()

# ========== BUAT TAB ==========
tab1, tab2 = st.tabs([
    "🎯 **PREDIKSI SNBP** (Seleksi Nilai Rapor)", 
    "📝 **PREDIKSI SNBT** (Seleksi Tes UTBK)"
])

# ========== TAB 1: SNBP ==========
with tab1:
    st.header("SISTEM PREDIKSI SNBP")
    st.caption("Berdasarkan nilai rapor semester 1-5 dan prestasi")
    st.divider()
    
    # INPUT SNBP
    col_snbp1, col_snbp2 = st.columns(2)
    
    with col_snbp1:
        st.subheader("📊 Nilai Rapor Semester 1-5")
        
        # Input 5 semester dengan number_input
        sem1 = st.number_input("Semester 1", 60, 100, 85, key="snbp_s1")
        sem2 = st.number_input("Semester 2", 60, 100, 86, key="snbp_s2")
        sem3 = st.number_input("Semester 3", 60, 100, 87, key="snbp_s3")
        sem4 = st.number_input("Semester 4", 60, 100, 88, key="snbp_s4")
        sem5 = st.number_input("Semester 5", 60, 100, 89, key="snbp_s5")
        
        # Hitung rata-rata
        rata_snbp = (sem1 + sem2 + sem3 + sem4 + sem5) / 5
        st.success(f"**Rata-rata nilai:** {rata_snbp:.1f}")
    
    with col_snbp2:
        st.subheader("🏆 Prestasi & Pilihan")
        
        prestasi_snbp = st.selectbox(
            "Prestasi Tertinggi",
            ["Tidak ada", "Juara kelas", "Olimpiade sekolah", 
             "Olimpiade kota/kabupaten", "Olimpiade provinsi", "Olimpiade nasional"],
            key="prestasi_snbp"
        )
        
        jurusan_snbp = st.selectbox(
            "Jurusan Target",
            ["Teknik Informatika", "Kedokteran", "Psikologi", 
             "Ekonomi", "Hukum", "Farmasi", "Teknik Sipil"],
            key="jurusan_snbp_tab"
        )
        
        ptn_snbp = st.selectbox(
            "PTN Target",
            ["UI", "ITB", "UGM", "UNPAD", "IPB", "UB", "UNS", "UNDIP"],
            key="ptn_snbp_tab"
        )
    
    # TOMBOL PREDIKSI SNBP
    if st.button("🎯 PREDIKSI SNBP", key="btn_snbp", type="primary", use_container_width=True):
        st.divider()
        st.subheader("📊 HASIL PREDIKSI SNBP")
        
        # LOGIKA SNBP
        skor = 0
        
        # 1. Nilai
        if rata_snbp >= 95: skor = 95
        elif rata_snbp >= 90: skor = 85
        elif rata_snbp >= 85: skor = 75
        elif rata_snbp >= 80: skor = 65
        elif rata_snbp >= 75: skor = 55
        else: skor = 45
        
        # 2. Prestasi
        if "nasional" in prestasi_snbp.lower(): skor += 20
        elif "provinsi" in prestasi_snbp.lower(): skor += 15
        elif "kota" in prestasi_snbp.lower() or "kabupaten" in prestasi_snbp.lower(): skor += 10
        elif "sekolah" in prestasi_snbp.lower(): skor += 5
        
        # 3. Kesulitan
        if jurusan_snbp in ["Kedokteran", "Teknik Informatika", "Farmasi"]:
            skor -= 15
        elif jurusan_snbp in ["Psikologi", "Arsitektur"]:
            skor -= 10
        
        if ptn_snbp in ["UI", "ITB", "UGM"]:
            skor -= 10
        
        # 4. Kategori
        if skor >= 80:
            kategori = "SANGAT Rasional"
            warna = "success"
        elif skor >= 65:
            kategori = "Cukup Rasional"
            warna = "info"
        elif skor >= 50:
            kategori = "KURANG RASIONAL"
            warna = "warning"
        else:
            kategori = "TIDAK RASIONAL"
            warna = "error"
        
        # TAMPILAN HASIL
        col_res1, col_res2 = st.columns([2, 1])
        
        with col_res1:
            if warna == "success":
                st.success(f"## ✅ {kategori}")
            elif warna == "info":
                st.info(f"## ⚡ {kategori}")
            elif warna == "warning":
                st.warning(f"## ⚠️ {kategori}")
            else:
                st.error(f"## ❌ {kategori}")
            
            st.write(f"**{jurusan_snbp} - {ptn_snbp}**")
        
        with col_res2:
            st.metric("Rata-rata", f"{rata_snbp:.1f}")
            st.metric("Indeks", f"{skor}/100")
        
        # REKOMENDASI
        st.divider()
        st.write("**💡 Rekomendasi:**")
        if kategori == "SANGAT LAYAK":
            st.write("Pertahankan konsistensi nilai. Fokus pada SNBP sebagai jalur utama.")
        elif kategori == "LAYAK":
            st.write("Tingkatkan nilai semester akhir. Siapkan alternatif.")
        elif kategori == "KURANG LAYAK":
            st.write("Pertimbangkan jurusan/PTN lain. Siapkan opsi SNBT.")
        else:
            st.write("Evaluasi ulang pilihan. Pertimbangkan jalur SNBT.")

# ========== TAB 2: SNBT ==========
with tab2:
    st.header("SISTEM PREDIKSI SNBT")
    st.caption("Berdasarkan skor UTBK: TPS, Literasi, dan Penalaran Matematika")
    st.divider()
    
    # INPUT SNBT - PAKAI NUMBER_INPUT SEPERTI SNBP
    col_snbt1, col_snbt2 = st.columns(2)
    
    with col_snbt1:
        st.subheader("📝 Skor UTBK (200-800)")
        
        # Input skor dengan number_input seperti SNBP
        tps = st.number_input(
            "TPS (Potensi Skolastik)", 
            min_value=200, 
            max_value=800, 
            value=650,
            step=10,
            key="tps_input",
            help="Nilai TPS antara 200-800"
        )
        
        literasi = st.number_input(
            "Literasi dalam Bahasa", 
            min_value=200, 
            max_value=800, 
            value=600,
            step=10,
            key="literasi_input",
            help="Nilai Literasi antara 200-800"
        )
        
        penalaran = st.number_input(
            "Penalaran Matematika", 
            min_value=200, 
            max_value=800, 
            value=550,
            step=10,
            key="penalaran_input",
            help="Nilai Penalaran antara 200-800"
        )
        
        # Tampilkan skor yang dimasukkan
        st.write("**Skor yang dimasukkan:**")
        st.write(f"- TPS: **{tps}/800**")
        st.write(f"- Literasi: **{literasi}/800**")
        st.write(f"- Penalaran: **{penalaran}/800**")
        
        # Hitung rata-rata
        rata_snbt = (tps + literasi + penalaran) / 3
        st.info(f"**Rata-rata skor:** {rata_snbt:.0f}/800")
    
    with col_snbt2:
        st.subheader("🎯 Pilihan Jurusan & PTN")
        
        jurusan_snbt = st.selectbox(
            "Jurusan Target",
            ["Teknik Informatika", "Kedokteran", "Psikologi", 
             "Ekonomi", "Hukum", "Farmasi", "Teknik Sipil",
             "Arsitektur", "Ilmu Komunikasi", "Akuntansi"],
            key="jurusan_snbt_tab"
        )
        
        ptn_snbt = st.selectbox(
            "PTN Target",
            ["UI", "ITB", "UGM", "UNPAD", "IPB", "UB", "UNS", "UNDIP",
             "UNBRAW", "UNJ", "UNY", "UNESA"],
            key="ptn_snbt_tab"
        )
        
        # Analisis kekuatan (berdasarkan input number)
        st.subheader("🔍 Analisis Kekuatan")
        st.write("**Kategori Skor:**")
        
        if tps >= 700:
            st.success("✅ **TPS: Unggul** (≥700)")
        elif tps >= 600:
            st.info("📊 **TPS: Baik** (600-699)")
        else:
            st.warning("📉 **TPS: Perlu ditingkatkan** (<600)")
            
        if literasi >= 700:
            st.success("✅ **Literasi: Unggul** (≥700)")
        elif literasi >= 600:
            st.info("📊 **Literasi: Baik** (600-699)")
        else:
            st.warning("📉 **Literasi: Perlu ditingkatkan** (<600)")
            
        if penalaran >= 700:
            st.success("✅ **Penalaran: Unggul** (≥700)")
        elif penalaran >= 600:
            st.info("📊 **Penalaran: Baik** (600-699)")
        else:
            st.warning("📉 **Penalaran: Perlu ditingkatkan** (<600)")
    
    # TOMBOL PREDIKSI SNBT
    if st.button("📝 PREDIKSI SNBT", key="btn_snbt", type="primary", use_container_width=True):
        st.divider()
        st.subheader("📊 HASIL PREDIKSI SNBT")
        
        # LOGIKA SNBT
        skor = 0
        rata_total = (tps + literasi + penalaran) / 3
        
        # 1. Rata-rata skor
        if rata_total >= 750: skor = 95
        elif rata_total >= 700: skor = 85
        elif rata_total >= 650: skor = 75
        elif rata_total >= 600: skor = 65
        elif rata_total >= 550: skor = 55
        else: skor = 45
        
        # 2. Kekuatan spesifik berdasarkan jurusan
        jurusan_eksakta = ["Teknik Informatika", "Kedokteran", "Farmasi", "Teknik Sipil", "Arsitektur"]
        jurusan_sosial = ["Psikologi", "Hukum", "Ilmu Komunikasi", "Ekonomi", "Akuntansi"]
        
        if jurusan_snbt in jurusan_eksakta:
            if penalaran >= 650: skor += 15
            elif penalaran >= 550: skor += 5
        elif jurusan_snbt in jurusan_sosial:
            if literasi >= 650: skor += 15
            elif literasi >= 550: skor += 5
        
        # 3. Jika semua komponen seimbang tinggi
        if tps >= 650 and literasi >= 650 and penalaran >= 650:
            skor += 10
        
        # 4. Kesulitan berdasarkan jurusan dan PTN
        jurusan_berat = ["Kedokteran", "Teknik Informatika", "Farmasi"]
        if jurusan_snbt in jurusan_berat:
            skor -= 15
        
        ptn_berat = ["UI", "ITB", "UGM"]
        if ptn_snbt in ptn_berat:
            skor -= 10
        
        # Pastikan skor dalam range 0-100
        skor = max(0, min(100, skor))
        
        # 5. Kategori
        if skor >= 80:
            kategori = "SANGAT Rasional"
            warna = "success"
        elif skor >= 65:
            kategori = "Cukup Rasional"
            warna = "info"
        elif skor >= 50:
            kategori = "KURANG RASIONAL"
            warna = "warning"
        else:
            kategori = "TIDAK RASIONAL"
            warna = "error"
        
        # TAMPILAN HASIL
        col_res1, col_res2, col_res3 = st.columns([2, 1, 1])
        
        with col_res1:
            if warna == "success":
                st.success(f"## ✅ {kategori}")
            elif warna == "info":
                st.info(f"## ⚡ {kategori}")
            elif warna == "warning":
                st.warning(f"## ⚠️ {kategori}")
            else:
                st.error(f"## ❌ {kategori}")
            
            st.write(f"**{jurusan_snbt} - {ptn_snbt}**")
        
        with col_res2:
            st.metric("Rata-rata Skor", f"{rata_total:.0f}")
        
        with col_res3:
            st.metric("Indeks Kelayakan", f"{skor}/100")
        
        # DETAIL SKOR
        st.divider()
        st.write("**📋 Detail Skor Anda:**")
        
        col_detail1, col_detail2, col_detail3 = st.columns(3)
        with col_detail1:
            st.metric("TPS", f"{tps}", delta="Target: ≥650" if tps >= 650 else None)
        with col_detail2:
            st.metric("Literasi", f"{literasi}", delta="Target: ≥600" if literasi >= 600 else None)
        with col_detail3:
            st.metric("Penalaran", f"{penalaran}", delta="Target: ≥600" if penalaran >= 600 else None)
        
        # REKOMENDASI SPESIFIK
        st.divider()
        st.subheader("💡 Rekomendasi Strategi")
        
        if kategori == "SANGAT Rasional":
            st.success("""
            **🎉 Profil sangat kompetitif!**
            1. **Fokus** pada jurusan pilihan pertama
            2. **Pertahankan** konsistensi skor
            3. **Ikuti try out** untuk menjaga performa
            """)
            
        elif kategori == "Cukup Rasional":
            st.info("""
            **📈 Profil cukup kompetitif**
            1. **Tingkatkan** bagian terlemah
            2. **Latihan soal** rutin setiap hari
            3. **Kelola waktu** dengan baik saat tes
            """)
            
        elif kategori == "KURANG RASIONAL":
            st.warning("""
            **⚠️ Perlu peningkatan signifikan**
            1. **Identifikasi** kelemahan utama
            2. **Ikut bimbingan belajar** intensif
            3. **Pertimbangkan** jurusan alternatif
            """)
            
        else:
            st.error("""
            **🚨 Perlu evaluasi mendalam**
            1. **Konsultasi** dengan mentor/guru
            2. **Fokus** pada peningkatan fundamental
            3. **Pertimbangkan** jalur mandiri/swasta
            """)
        
        # REKOMENDASI BERDASARKAN JURUSAN
        st.divider()
        st.write("**🎯 Rekomendasi berdasarkan jurusan:**")
        
        if jurusan_snbt in jurusan_eksakta:
            if penalaran < 600:
                st.warning(f"⚠️ **Untuk {jurusan_snbt}, Penalaran Anda ({penalaran}) perlu ditingkatkan minimal ke 600+**")
            else:
                st.success(f"✅ **Penalaran ({penalaran}) sudah memadai untuk {jurusan_snbt}**")
                
        elif jurusan_snbt in jurusan_sosial:
            if literasi < 600:
                st.warning(f"⚠️ **Untuk {jurusan_snbt}, Literasi Anda ({literasi}) perlu ditingkatkan minimal ke 600+**")
            else:
                st.success(f"✅ **Literasi ({literasi}) sudah memadai untuk {jurusan_snbt}**")

# ========== FOOTER ==========
st.divider()
st.caption("""
🔬 **Sistem Prediksi Seleksi Masuk PTN** | Prototipe untuk Skripsi  
⚠️ *Hasil prediksi menggunakan logika sederhana. Pada sistem final akan menggunakan algoritma C4.5 dengan data historis.*
""")