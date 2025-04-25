"""
File: lab2.py
Sets the Instructions file for the lab.
Adds function calling tools to the agent's toolset.
Add a file search tool to the agent's toolset.
"""

from azure.ai.projects.models import FileSearchTool

from labs.lab_base import LabBase

INSTRUCTIONS_FILE = "instructions/file_search.txt"
TENTS_DATA_SHEET_FILE = "datasheet/contoso-tents-datasheet.pdf"


class Lab2(LabBase):
    def __init__(self) -> None:
        super().__init__(INSTRUCTIONS_FILE)

    async def add_agent_tools(self) -> None:
        """Add tools to the agent's toolset."""

        # Add function calling tools to the agent's toolset
        self.toolset.add(self.functions)

        # Create a vector store and add the Tents Data Sheet file to it
        vector_store = await self.utilities.create_vector_store(
            self.project_client,
            files=[TENTS_DATA_SHEET_FILE],
            vector_store_name="Contoso Product Information Vector Store",
        )

        # Add the file search tool to the agent's toolset
        file_search_tool = FileSearchTool(vector_store_ids=[vector_store.id])
        self.toolset.add(file_search_tool)
