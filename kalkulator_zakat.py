import streamlit as st

st.title("Kalkulator Zakat Penghasilan")
st.write("---")
st.write("Semoga Kalkulator Zakat Dapat Membantu!^^")
#input 1
    a = st.number_input("Masukkan Penghasilan/Bulan")
    b = st.number_input("Penghasilan Lainnya/Bulan")
    c = st.number_input("Hutang/Cicilan")
    d = st.number_input("Jumlah Penghasilan/Bulan")

    st.title("Nisab Zakat Penghasilan")
    st.write("Nisab merupakan batas minimum jumlah harta yang harus terpenuhi agar dapat dianggap sebagai")
    st.write("harta yang wajib dizakati. Zakat hanya diberlakukan pada penghasilan yang melampaui nisab")
    st.write("tersebut. Untuk Zakat Penghasilan, nisab yang ditetapkan setara dengan 85 gram emas.")
    a = st.number_input("Harga Emas Saat Ini (per Gram)")
    b = st.number_input("Besar Nisab Zakat Penghasilan/Bulan")
    c = st.number_input("Wajib/Tidak Membayar Zakat Penghasilan:")
    d = st.number_input("Jumlah yang Perlu Dibayarkan/Bulan")
    wealth = st.number_input("Total kekayaan Anda (dalam rupiah)")
    nisab = st.number_input("Nisab (dalam rupiah)", value=0)

    if st.button("Hitung"):
        result = calculate_zakat(nisab, wealth)
        st.write(result)

if __name__ == "__main__":
    main()
