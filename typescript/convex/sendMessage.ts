import { mutation } from "./_generated/server";

type Message = {
  body: string;
  author: string;
};

export default mutation(
  async ({ db }, { body, author }: Message) => {
    const message = { body, author };
    await db.insert("messages", message);
  }
);
