import streamlit as st
import yaml

# Install required packages
st.write("Installing required packages...")
st.script_runner.install_py_package('pyyaml')


# Rest of the script...

# Create a file uploader for YAML files
yaml_file = st.file_uploader("Upload YAML File", type="yaml")

if yaml_file:
    # Load the YAML content from the file
    yaml_content = yaml_file.read()

    # Parse the YAML content
    data = yaml.safe_load(yaml_content)

    # Extract the metadata fields
    metadata = data.get("metadata", {})
    name = metadata.get("name", "")
    namespace = metadata.get("namespace", "")

    # Form inputs for modifying metadata fields
    updated_name = st.text_input("Name", value=name)
    updated_namespace = st.text_input("Namespace", value=namespace)

    # Update the metadata fields in the YAML content
    metadata["name"] = updated_name
    metadata["namespace"] = updated_namespace

    # Save the updated YAML content
    updated_content = yaml.safe_dump(data)

    # Button to download the modified YAML file
    st.download_button("Download Updated YAML", data=updated_content.encode(), file_name="updated.yaml", mime="text/yaml")
