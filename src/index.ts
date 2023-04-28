#!/usr/bin/env node

import { Command } from 'commander'
import langChainClient from './core/langchainClient';

const program = new Command()

program
          .command('search <prompt>')
  .description('chat with chatGPT!')
  .action(async (prompt) => {
    await langChainClient.openAiChain(prompt)
  })

program.parseAsync(process.argv)
