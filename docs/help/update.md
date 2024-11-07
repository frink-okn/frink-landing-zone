# Update Your Graph in FRINK


To ensure a smooth and automated deployment of data pipelines, establishing structured rules and policies around branch and tag usage in our data repositories is essential. This guide focuses on implementing best practices for versioning datasets and aligning the workflows for raw and stable data processing. By following these guidelines, teams can leverage FRINK's lakeFS repository version control capabilities more efficiently and streamline their automatic deployment processes.

### **Repository Structure**

Each LakeFS repository should house a single dataset to allow for independent versioning and easier maintenance. This approach is different from assigning a repository per team, which can complicate the versioning process if multiple datasets are housed in the same repository. 

  
### **Branching Strategy**

The branching strategy revolves around separating the stages of data processing into different branches to ensure clarity and facilitate automation.

#### Main Branch
- **Purpose**: Holds the final, stable dataset.
- **Initial State**: Contains no data on first creation.
- **Access Control**: Protected branch—only allows merge requests (no direct commits).
  
#### Develop Branch
- **Purpose**: Serves as the working branch for raw data.
- **Usage**: Data owners make changes here, after which a merge is made into the main branch.
  
#### Stable Branch
- **Purpose**: Contains processed and validated datasets ready for deployment. These branches are used by FRINK's automation tools.
- **Naming Convention**: follow the format `stable_vX_X_X` (e.g., `stable_v0_90_1`).
- **Usage**: Acts as an intermediary for processed datasets before being deployed to FRINK database servers.

### **Workflows and Processing**
!!! info inline end ""	

    The following data formats are currently supported
    <br>
    - Single Neo4j dump files in single repository (WIP)
    <br>
    - Multiple RDF file with the following extensions : rdf, xml, ttl, nt, nq, jsonld, json, rj, trig, trix, n3 
    <br>
    - Single HDT (WIP)


Different workflows will manage the transition of raw data to stable datasets in HDT format (preferred by the FRINK system). These workflows can involve data conversion, preprocessing, or other transformations necessary for your system.

    
??? Note
   
    Please make sure the contents of your files match standard file extensions. The automation pipelines are sensetive to file extensions.


#### Workflow Process:
1. **Merge to Main**: When raw data on the `develop` branch is merged into the `main` branch, conversion workflow is triggered. 
2. **Conversion**: The workflow processes raw data into the stable format (HDT).
3. **Stable Branch Creation**: Upon successful processing, a new `stable` branch is created, following the `stable_v*` naming convention.
4. **Tagging**: After successful push, the stable branch is tagged with the corresponding version number.

### **Tagging and Version Control**

Tags provide a crucial mechanism for keeping track of stable dataset releases. The tag on the main branch represents an official release of the dataset and will trigger deployment pipelines.

#### Tagging Process:
- **Automated Tag Creation**: Tags can be automatically created after successful validation of the dataset. This ensures data reliability and minimizes manual intervention.
- **Naming Convention**: Tags should follow the version format used in the stable branch, such as `v0_90_1` reformatted to `v0.90.1`.

### **Events Triggering Automation**

To achieve automated deployment, two key events can be monitored:

#### Event 1: Merge from Develop to Main
- **Trigger**: Merging raw data from the `develop` branch to the `main` branch triggers ETL pipelines.
- **ETL Output**: Once the ETL process is complete, the system pushes the new dataset onto a `stable` branch.

#### Event 2: Tag Creation
- **Trigger**: Tag is created, marking the official release of the dataset.
- **Deployment**: The creation of this tag initiates an automatic deployment process, loading the new dataset.


### **Summary of Versioning Workflow**
1. **Graph Data**: Changes made in the `develop` branch by data owners.
2. **Merge to Main**: Graph data is merged into the `main` by data owners.
3. **Processing**: Automation triggers conversion pipelines to process incoming data.
4. **Stable Dataset**: Automation HDT format of new data is pushed to a new `stable` branch.
6. **Tagging**: `stable` branch is automatically tagged with the corresponding version number.
7. **Deployment**: The tag creation triggers an automatic deployment process.

