import streamlit as st

# Define the form inputs
deployment_name = st.text_input("Deployment Name", value="elk-deployment")
namespace = st.text_input("Namespace", value="default")
replicas = st.number_input("Replicas", min_value=0, value=1)
image_names = {
    "elasticsearch": "elasticsearch:7.12.1",
    "logstash": "logstash:7.12.1",
    "kibana": "kibana:7.12.1",
}
container_configs = {}
for container in image_names:
    container_image = image_names[container]
    # Prompt for container configurations (e.g., resources, environment variables, volume mounts)
    container_configs[container] = {
        "image": container_image,
        # Add relevant configurations here
    }

# Generate the YAML content based on form inputs
yaml_content = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {deployment_name}
  namespace: {namespace}
spec:
  replicas: {replicas}
  selector:
    matchLabels:
      app: elk-app
  template:
    metadata:
      labels:
        app: elk-app
    spec:
      containers:
"""
for container in container_configs:
    image = container_configs[container]["image"]
    # Add container configurations (e.g., resources, environment variables, volume mounts) to YAML content

# Display the generated YAML content
st.subheader("Generated YAML Content:")
st.code(yaml_content, language="yaml")
