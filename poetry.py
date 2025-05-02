import streamlit as st

# st.title("Poetry App")

choice = st.radio("Choose what you want 👇",
         ['Add new poetry', 'Show all poetry', 'Search poetry by name'])

if choice == "Add new poetry":
    st.write("Add New Poetry")
    name= st.text_input("Enter poet Name")
    poetry=st.text_input("Enter poetry: ")
    if st.button('Save poetry'):
        with open("poet.txt","a") as f:
            f.write(f"{name}: {poetry}\n")
        st.success("Poet saved!")
elif choice == "Show all poetry":
    st.write("Show All Poetry")
    with open("poet.txt", "r") as f:
        content = f.read()
        st.text_area('poetry content', content, height =  200, disabled=True)
elif choice == "Search poetry by name":
    st.write("Search Poet by Name")
    name = st.text_input("Enter poet name")
    with open("poet.txt","r")as f:
        lines = f.readlines()
        f.close()
        found = False
        for line in lines:
            if name.lower() in line.lower():
                st.write(line.strip())
                found = True
        if not found:
            st.write("No poet found with that name.")
    
