import { OpenAI } from "langchain/llms/openai";
import { green } from "colorette"


const LangChainClient: () => ILangChainClient = () => {
  return {
    openAiChain: async (prompt: string): Promise<void> => {
      const model = new OpenAI({ openAIApiKey: process.env.OPENAI_API_KEY });

      if (!prompt) {
        throw new Error("Prompt is required");
      }

      const res = await model.call(
        prompt
      );

      console.log(green(`>> ${res}`));

    },
  }

}


interface ILangChainClient {
  openAiChain: (prompt: string) => Promise<void>;
}

const langChainClient = LangChainClient()
export default langChainClient

