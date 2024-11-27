# Field Manager python client

## What is this?

The Field Manager (FM) Python client is a library designed to provide developers with programmatic access to the Field Manager API. This client streamlines interactions with the API, enabling users to perform various operations, such as retrieving project data, managing locations, and automating data workflows directly from Python code.

### Purpose

The purpose of the FM Python client is to simplify integration with the Field Manager platform, allowing end users to automate and scale interactions with Field Manager resources. By using this client, developers can efficiently incorporate Field Manager data and functionality into their own applications and workflows, reducing the need for manual API calls.

### What does this client provide

The FM Python client offers complete access to all API entry points and data models provided by the Field Manager platform. This comprehensive access allows developers to work with any part of the Field Manager API, ensuring they can interact with all available endpoints and data structures in a streamlined and intuitive way.

The client’s structure and design follow a Pythonic approach, making it easy to use for Python developers. Each endpoint is accessible through dedicated methods, and data models are represented with clear, well-defined classes. This setup minimizes the need to write low-level code to handle HTTP requests or parse JSON responses, allowing end users to focus on building solutions and integrating Field Manager functionalities directly into their applications.

### Generation and Maintenance

This client is automatically generated from the Field Manager API’s OpenAPI specification. This means that as the API evolves, the client can be quickly regenerated to stay up-to-date with the latest changes, minimizing the need for manual updates and ensuring ongoing compatibility with Field Manager’s API. This automatic generation also helps with maintenance, as updates are reflected in the client with each new release of the API specification.

## How does this work?

Follow [this README](./field-manager-python-client/README.md) file and [this get organizations example](./examples/examples/ex_get_organizations.py) to play with this client.
