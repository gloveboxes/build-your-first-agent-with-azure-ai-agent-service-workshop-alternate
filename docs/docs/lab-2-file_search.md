## Introduction

Grounding a conversation with documents is highly effective, especially for retrieving product details that may not be available in an operational database. The Azure AI Agent Service includes a [File Search tool](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/file-search){:target="_blank"}, which enables agents to retrieve information directly from uploaded files, such as user-supplied documents or product data, enabling a [RAG-style](https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation){:target="_blank"} search experience.

In this lab, you'll learn how to enable the document search and upload the Tents Data Sheet to a vector store for the agent. Once activated, the tool allows the agent to search the file and deliver relevant responses. Documents can be uploaded to the agent for all users or linked to a specific user thread, or linked to the Code Interpreter.

When the app starts, a vector store is created, the Contoso tents datasheet PDF file is uploaded to the vector store, and it is made available to the agent.

Normally, you wouldn’t create a new vector store and upload documents each time the app starts. Instead, you’d create the vector store once, upload potentially thousands of documents, and connect the store to the agent.

A [vector store](https://en.wikipedia.org/wiki/Vector_database){:target="_blank"} is a database optimized for storing and searching vectors (numeric representations of text data). The File Search tool uses the vector store for [semantic search](https://en.wikipedia.org/wiki/Semantic_search){:target="_blank"} to search for relevant information in the uploaded document.

## Lab Exercise

1. Open the **shared/datasheet/contoso-tents-datasheet.pdf** file from VS Code. The PDF file includes detailed product descriptions for the tents sold by Contoso.

2. **Review** the file’s contents to understand the information it contains, as this will be used to ground the agent’s responses.

=== "Python"

    1. Open the `main.py`.
    2. Set the lab number to 2 in the `main.py` file.

        ```python
        # Set your lab:
        LAB_NUMBER = 2
        ```

    2. Review the code in `labs/lab2.py`. It:

        1. Sets the **instruction file**.
        2. Adds **function calling** and **file search** to the agent app.

        ```python
        {% include-markdown "../../src/python/workshop/labs/lab2.py" %}
        ```

=== "C#"

      1. Open the `Program.cs` file.
      2. **Update** the creation of the lab to use the `Lab3` class.

          ```csharp
          await using Lab lab = new Lab2(projectClient, apiDeploymentName);
          ```

      3. Review the `Lab3.cs` class to see how `InitialiseLabAsync` is used to add the PDF to a vector store and add the File Search tool to the agent, and `InitialiseToolResources` is used to add the File Search tool to the agent. These methods would be good places to add breakpoints to observe the process.

## Review the Instructions

1. Review the **create_vector_store** function in the **utilities.py** file. The create_vector_store function uploads the Tents Data Sheet and saves it in a vector store.

    If you are comfortable using the VS Code debugger, then set a [breakpoint](https://code.visualstudio.com/Docs/editor/debugging){:target="_blank"} in the **create_vector_store** function to observe how the vector store is created.

2. Open the **shared/instructions/file_search.txt** file.

    Review the updates in the **Tools** section of the instructions file compared with the one we have used in the previous step.


## Run the Agent App

1. Press <kbd>F5</kbd> to run the app.
1. In the terminal, the app starts, and the agent app will prompt you to **Enter your query**.

### Start a Conversation with the Agent

The following conversation uses data from both the Contoso sales database and the uploaded Tents Data Sheet, so the results will vary depending on the query.

1. **What brands of hiking shoes do we sell?**

    !!! info
        We haven't provided the agent with any files containing information about hiking shoes.

        In the first lab you may have noticed that the transaction history from the underlying database did not include any product brands or descriptions, either.

1. **What brands of tents do we sell?**

    The agent responds with a list of distinct tent brands mentioned in the Tents Data Sheet.

    !!! info
        The agent can now reference the provided data sheet to access details such as brand, description, product type, and category, and relate this data back to the Contoso sales database.

1. **What product type and categories are these brands associated with?**

    The agent provides a list of product types and categories associated with the tent brands.

1. **What were the sales of tents in 2024 by product type? Include the brands associated with each.**

    !!! info
        It's possible the agent might get this wrong, and suggest incorrectly that AlpineGear has a Family Camping tent. To address this, you could provide further context in the instructions or the datasheet, or provide context to the agent directly as in next prompt. For example, try the following:
        "**Contoso does not sell Family Camping tents from AlpineGear. Try again.**"

1. **What were the sales of AlpineGear in 2024 by region?**

    The agent responds with sales data from the Contoso sales database.

    !!! info
        The agent interprets this as a request to find all sales of tents in the "CAMPING & HIKING' category, since it
        now has access to information that Alpine Gear is a brand of backpacking tent.

## Stop the Agent App

When you're done, type **exit** to clean up the agent resources and stop the app.
