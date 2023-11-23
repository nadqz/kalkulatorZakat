import streamlit as st

def zakat_penghasilan():
    st.title("Kalkulator Zakat Penghasilan")
    st.write("---")
    st.write("Zakat penghasilan atau zakat profesi adalah zakat yang wajib dibayarkan atas pendapatan yang diperoleh dari pekerjaan atau profesi, sepeti gaji. Zakat penghasilan termasuk dalam kategori zakat mal, yang merupakan kewajiban membayar zakat karena memiliki atau menyimpan harta seperti uang dan emas.")

    #Input Penghasilan per Bulan
    penghasilan_bulanan = st.number_input("Penghasilan per Bulan (IDR)")

    #Input Penghasilan Lainnya per Bulan
    penghasilan_lainnya = st.number_input("Penghasilan Lainnya per Bulan (IDR)")

    #Input Hutang atau Cicilan
    hutang_cicilan = st.number_input("Hutang atau Cicilan per Bulan (IDR)")

    #Menghitung Jumlah Penghasilan Setelah Dikurangi Hutang atau Cicilan
    penghasilan_setelah_hutang = penghasilan_bulanan + penghasilan_lainnya - hutang_cicilan

    #Menampilkan Jumlah Penghasilan yang Telah Dikalkulasi
    st.write("Jumlah Penghasilan Bersih per Bulan: ", penghasilan_setelah_hutang, "IDR")
    
    st.title("Nisab Zakat Penghasilan")
    st.write("Nisab merupakan batas minimum jumlah harta yang harus terpenuhi agar dapat dianggap sebagai harta yang wajib dizakati. Zakat hanya diberlakukan pada penghasilan yang melampaui nisab tersebut. Untuk Zakat Penghasilan, nisab yang ditetapkan setara dengan 85 gram emas.")
    st.header("Niat Zakat Penghasilan")
    st.subheader("نَوَيْتُ أَنْ أُخْرِجَ زَكَاةَ مَالِى فَرْضًا لِلَّهِ تَعَالَى")
    st.caption("Nawaitu an ukhrija zakatadz maali fardhan lillahi ta’ala.")
    st.write("Artinya: Aku niat mengeluarkan zakat hartaku fardhu karena Allah Ta'ala.")

    #Input Harga Emas Saat Ini per Gram
    harga_emas = st.number_input("Harga Emas Saat Ini per Gram (IDR)")

    #Menentukan Apakah Harga Emas Bernilai 0
    if harga_emas == 0:
        st.write("Harga Emas Tidak Boleh Bernilai 0")
        return
    
    #Menghitung Besaran Nishab Zakat Penghasilan per Bulan
    nisab_penghasilan = (85 / 12 * harga_emas)
    st.write("Besaran Nishab Zakat Penghasilan per Bulan: ", nisab_penghasilan, "IDR")

    #Memeriksa Penghasilan Setelah Hutang lebih besar daripada Nisab
    if penghasilan_setelah_hutang >= nisab_penghasilan:
        st.write("Penghasilan Anda melebihi Nisab untuk Zakat Penghasilan.")

    # Hitung Zakat
        zakat_amount = 0.025 * penghasilan_setelah_hutang
        st.write("Jumlah Zakat Penghasilan yang Harus Dibayarkan: ", zakat_amount, "IDR")
    else:
        st.write("Penghasilan Anda belum mencapai Nisab untuk Zakat Penghasilan.")
        
# Run the function
zakat_penghasilan()
